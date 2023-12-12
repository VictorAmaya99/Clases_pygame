#Codigo que hace rebotar a un rectangulo

import pygame
from sys import exit

from config import *

pygame.init()

clock = pygame.time.Clock()

#Configuracion de pantalla principal:
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

# Creamos el bloque:
block = pygame.Rect(300,500,100,50)
block_color = RED
block_dir = DOWN_LEFT


is_runnig = True


while is_runnig:
    clock.tick(FPS)
    # Detectar los eventos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runnig = False

    # Actualizar los elementos:

    # Controlo rebotes y cambio de direccion
    # Rebote derecha pantalla: 
    if block.right >= WIDTH:
        if block_dir == DOWN_RIGHT:
            block_dir = DOWN_LEFT
        elif block_dir == UP_RIGHT:
            block_dir = UP_LEFT
    # Rebote izquierda pantalla:
    elif block.left <= 0:
        if block_dir == DOWN_LEFT:
            block_dir = DOWN_RIGHT
        elif block_dir == UP_LEFT:
            block_dir = UP_RIGHT
   # Rebote abajo pantalla:
    elif block.bottom >= HEIGHT:
        if block_dir == DOWN_RIGHT:
            block_dir = UP_RIGHT
        if block_dir == DOWN_LEFT:
            block_dir = UP_LEFT
    # Rebote arriba pantalla:
    elif block.top <= 0:
        if block_dir == UP_LEFT:
            block_dir = DOWN_LEFT
        elif block_dir == UP_RIGHT:
            block_dir = DOWN_RIGHT
    
    # Muevo el rectangulo de acuerdo a su direccion:
    if block_dir == DOWN_RIGHT:
        block.left += SPEED
        block.top += SPEED 
    elif block_dir == DOWN_LEFT:
        block.left -= SPEED
        block.top += SPEED
    elif block_dir == UP_LEFT:
        block.left -= SPEED
        block.top -= SPEED
    elif block_dir == UP_RIGHT:
        block.left += SPEED
        block.top -= SPEED


    # Dibujar pantalla:
    screen.fill(BLACK) # La pantalla se pinta cada vez que hay una interaccion, se pinta primero la pared y despues el rectangulo
    pygame.draw.rect(screen, block_color, block)

    pygame.display.flip()
 
pygame.quit()
exit()