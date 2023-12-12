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

edge = 0
radius = -1

# Creamos el bloque en un diccionario: (es mas eficiente)
blocks = [{"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT),
           "color": aleatory(), "dir": DOWN_LEFT}, 
           {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT),
           "color": aleatory(), "dir": DOWN_LEFT},
           {"rect": pygame.Rect(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, BLOCK_HEIGHT),
           "color": aleatory(), "dir": DOWN_LEFT}
          ]

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
            block["color"] = aleatory()
            edge = randrange(20)
        # Rebote izquierda pantalla:
        elif block["rect"].left <= 0:
            if block["dir"] == DOWN_LEFT:
                block["dir"] = DOWN_RIGHT
            elif block["dir"] == UP_LEFT:
                block["dir"] = UP_RIGHT
            block["color"] = aleatory()
            radius = randrange(25)
        # Rebote abajo pantalla:
        elif block["rect"].bottom >= HEIGHT:
            if block["dir"] == DOWN_RIGHT:
                block["dir"] = UP_RIGHT
            if block["dir"] == DOWN_LEFT:
                block["dir"] = UP_LEFT
            block["color"] = aleatory()
        # Rebote arriba pantalla:
        elif block["rect"].top <= 0:
            if block["dir"] == UP_LEFT:
                block["dir"] = DOWN_LEFT
            elif block["dir"] == UP_RIGHT:
                block["dir"] = DOWN_RIGHT
            block["color"] = aleatory() 
    
    # Muevo el rectangulo de acuerdo a su direccion:
    for block in blocks:
        if block["dir"] == DOWN_RIGHT:
            block["rect"].left += SPEED
            block["rect"].top += SPEED 
        elif block["dir"] == DOWN_LEFT:
            block["rect"].left -= SPEED
            block["rect"].top += SPEED
        elif block["dir"] == UP_LEFT:
            block["rect"].left -= SPEED
            block["rect"].top -= SPEED
        elif block["dir"] == UP_RIGHT:
            block["rect"].left += SPEED
            block["rect"].top -= SPEED


    # Dibujar pantalla:
    screen.fill(BLACK) # La pantalla se pinta cada vez que hay una interaccion, se pinta primero la pared y despues el rectangulo
    for block in blocks:
        pygame.draw.rect(screen, block["color"], block["rect"], edge, radius)

    pygame.display.flip()
 
pygame.quit()
exit()