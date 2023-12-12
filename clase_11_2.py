# Se hizo una lista de diccionarios para manejar el rectangulo para hacer multiples bloques 

import pygame
from random import randint, randrange
from sys import exit
from config import *
from functions import *
from collisions import *

pygame.init()

clock = pygame.time.Clock()

#Configuracion de pantalla principal: 
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

speed_x = 5
speed_y = 5

coin_size = 30

count = 0

font = pygame.font.SysFont(None, 48)

text = font.render(f"Coins: {count}", True, MAGENTA)
text_rect = text.get_rect()
text_rect.midtop = (WIDTH // 2 , 30)

# crear un bloque
block = generate_block(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, 
                                 BLOCK_HEIGHT, aleatory())
is_runnig = True

# crear lista de coins:
coins = []
for i in range(25):
    coins.append(generate_block(randint(0, WIDTH - coin_size), randint(0, HEIGHT - coin_size), coin_size, 
                                 coin_size, YELLOW, radius=coin_size//2))

while is_runnig:
    clock.tick(FPS)
    # Detectar los eventos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runnig = False

    # Actualizar los elementos:

    # Controlo rebotes y cambio de direccion
    
    
    # Rebote derecha pantalla: 
    if block["rect"].right >= WIDTH:
        if block["dir"] == DOWN_RIGHT:
            block["dir"] = DOWN_LEFT
        elif block["dir"] == UP_RIGHT:
            block["dir"] = UP_LEFT
        # block["color"] = aleatory()
        # block["edge"] = randrange(20)
        # block["speed_x"] = randint(1,10)
    # Rebote izquierda pantalla:
    elif block["rect"].left <= 0:
        if block["dir"] == DOWN_LEFT:
            block["dir"] = DOWN_RIGHT
        elif block["dir"] == UP_LEFT:
            block["dir"] = UP_RIGHT
        # block["color"] = aleatory()
        # block["radius"] = randrange(25)
        # block["speed_x"] = randint(1,10)
    # Rebote abajo pantalla:
    elif block["rect"].bottom >= HEIGHT:
        if block["dir"] == DOWN_RIGHT:
            block["dir"] = UP_RIGHT
        if block["dir"] == DOWN_LEFT:
            block["dir"] = UP_LEFT
        # block["color"] = aleatory()
        # block["speed_y"] = randint(1,10)
    # Rebote arriba pantalla:
    elif block["rect"].top <= 0:
        if block["dir"] == UP_LEFT:
            block["dir"] = DOWN_LEFT
        elif block["dir"] == UP_RIGHT:
            block["dir"] = DOWN_RIGHT
        # block["color"] = aleatory()
        # block["speed_y"] = randint(1,10)
    
    # Muevo el rectangulo de acuerdo a su direccion:
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
    
    for coin in coins [ : ]:
        if collision_detector(coin["rect"], block["rect"]):
            coins.remove(coin)
            count += 1
            text = font.render(f"Coins: {count}", True, MAGENTA)
            text_rect = text.get_rect()
            text_rect.midtop = (WIDTH // 2 , 30)


    # Dibujar pantalla:
    screen.fill(BLACK) # La pantalla se pinta cada vez que hay una interaccion, se pinta primero la pared y despues el rectangulo

    for coin in coins:
        pygame.draw.rect(screen, coin["color"], coin["rect"], coin["edge"], coin["radius"])

    pygame.draw.rect(screen, block["color"], block["rect"], block["edge"], block["radius"])

    # Blitear para poner el texto:
    screen.blit(text, text_rect)

    pygame.display.flip()
 
pygame.quit()
exit()