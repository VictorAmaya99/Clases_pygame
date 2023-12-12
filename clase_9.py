#En esta clase se hizo rebotar el rectangulo de arriba hacia abajo, y de un costado a otro
    

import pygame
from sys import exit

from config import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")


is_runnig = True

# rect_1 = pygame.Rect(10, 10, 200, 100)
# rect_2 = (200,200,300,150)

y_pos_1 = HEIGHT // 2 - height / 2
x_pos_1 = 300

y_pos_2 = 250
x_pos_2 = 0



going_down = True
slide = True

while is_runnig:
    clock.tick(FPS)
    # Detectar los elementos:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_runnig = False

    # Actualizar los elementos:

    if going_down:
        if y_pos_1 < HEIGHT - height: #Sirve para que el rectangulo baje
            y_pos_1 += SPEED
        else:
            going_down = False
    else:
        if y_pos_1 > 0:          #Sirve para que el rectangulo suba
            y_pos_1 -= SPEED
        else:
            going_down = True 

    if slide:
        if x_pos_2 < WIDTH - width: #Sirve para que el rectangulo baje
            x_pos_2 += SPEED
        else:
            slide = False
    else:
        if x_pos_2 > 0:          #Sirve para que el rectangulo suba
            x_pos_2 -= SPEED
        else:
            slide = True 

    screen.fill(LIGHT_PINK) # La pantalla se pinta cada vez que hay una interaccion, se pinta primero la pared y despues el rectangulo
    rect_a = pygame.draw.rect(screen, RED, (x_pos_1, y_pos_1, width, height), 5) # se pome el rectangulo en una variable rect_a para poder hacer otras cosas.
    rect_b = pygame.draw.rect(screen, BLUE, (x_pos_2, y_pos_2, width, height),5)

    #pygame.draw.line(screen, RED, (0,0), rect_a.topleft)
    
 

    pygame.display.flip()



    # x = pygame.draw.rect(screen, GREEN, rect_1, 5)
    # y = pygame.draw.rect(screen, YELLOW, rect_2)
            

pygame.quit()
exit()