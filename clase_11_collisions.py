# Se hizo una lista de diccionarios para manejar el rectangulo para hacer multiples bloques 

import pygame
from random import randint, randrange
from sys import exit
from config import *
from functions import *

pygame.init()

clock = pygame.time.Clock()

#Configuracion de pantalla principal: 
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

speed_x = 5
speed_y = 5

# Creamos bloques con las funcion creadora de bloques:
blocks = []

for i in range(2):
    blocks.append(generate_block(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), randint(20, BLOCK_WIDTH), 
                                 randint(20, BLOCK_HEIGHT), aleatory()))


# blocks = []
# b1 = generate_block()
# blocks.append(b1)

# blocks = [{"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT),
#            "color": aleatory(), "dir": DOWN_LEFT}, 
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT),
#            "color": aleatory(), "dir": DOWN_LEFT},
#            {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT),
#            "color": aleatory(), "dir": DOWN_LEFT}


is_runnig = True


while is_runnig:
    clock.tick(FPS)
    # Detectar los eventos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runnig = False

    # Actualizar los elementos:

    # Controlo rebotes y cambio de direccion
    
    for block in blocks:
        # Rebote derecha pantalla: 
        if block["rect"].right >= WIDTH:
            if block["dir"] == DOWN_RIGHT:
                block["dir"] = DOWN_LEFT
            elif block["dir"] == UP_RIGHT:
                block["dir"] = UP_LEFT
            # block["color"] = aleatory()
            block["edge"] = randrange(20)
            block["speed_x"] = randint(1,10)
        # Rebote izquierda pantalla:
        elif block["rect"].left <= 0:
            if block["dir"] == DOWN_LEFT:
                block["dir"] = DOWN_RIGHT
            elif block["dir"] == UP_LEFT:
                block["dir"] = UP_RIGHT
            # block["color"] = aleatory()
            block["radius"] = randrange(25)
            block["speed_x"] = randint(1,10)
        # Rebote abajo pantalla:
        elif block["rect"].bottom >= HEIGHT:
            if block["dir"] == DOWN_RIGHT:
                block["dir"] = UP_RIGHT
            if block["dir"] == DOWN_LEFT:
                block["dir"] = UP_LEFT
            # block["color"] = aleatory()
            block["speed_y"] = randint(1,10)
        # Rebote arriba pantalla:
        elif block["rect"].top <= 0:
            if block["dir"] == UP_LEFT:
                block["dir"] = DOWN_LEFT
            elif block["dir"] == UP_RIGHT:
                block["dir"] = DOWN_RIGHT
            # block["color"] = aleatory()
            block["speed_y"] = randint(1,10)
    
    # Muevo el rectangulo de acuerdo a su direccion:
    for block in blocks:
        if block["dir"] == DOWN_RIGHT:
            block["rect"].left += speed_x
            block["rect"].top += speed_y 
        elif block["dir"] == DOWN_LEFT:
            block["rect"].left -= speed_x
            block["rect"].top += speed_y
        elif block["dir"] == UP_LEFT:
            block["rect"].left -= speed_x
            block["rect"].top -= speed_y
        elif block["dir"] == UP_RIGHT:
            block["rect"].left += speed_x
            block["rect"].top -= speed_y

    # Para detectar colision:
    if collision_detector(blocks[0]["rect"], blocks[1]["rect"]):
        print("COLLISION" )
        #Para que cambien de color al colicionar:
        for block in blocks:
            block["color"] = aleatory()
    

    # Dibujar pantalla:
    screen.fill(BLACK) # La pantalla se pinta cada vez que hay una interaccion, se pinta primero la pared y despues el rectangulo
    for block in blocks:
        pygame.draw.rect(screen, block["color"], block["rect"], block["edge"], block["radius"])

    pygame.display.flip()
 
pygame.quit()
exit()