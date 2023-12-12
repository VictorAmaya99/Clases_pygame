import pygame
from random import randint, randrange
from sys import exit
from config import *
from functions import *
from collisions import *
from pygame.locals import * 

def mostrar_texto(superficie, texto, x, y, font_size=36, color=(0,0,0)):
    fuente = pygame.font.SysFont("comicsans", font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center=(x,y))
    superficie.blit(render, rect_texto)

#Inicializar los modulos de pygame
pygame.init()

#Configuracion de pantalla principal: 
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Mascaras")

player = pygame.transform.scale(pygame.image.load("./src/assets/ovni.png"), (200,200))
rect_player = player.get_rect()
mask_player = pygame.mask.from_surface(player)

asteroid = pygame.transform.scale(pygame.image.load("./src/assets/asteroide1.png"), (200,200))
rect_asteroid = asteroid.get_rect()
rect_asteroid.center = CENTER
mask_asteroid = pygame.mask.from_surface(asteroid)

# Crear un reloj
clock = pygame.time.Clock()

running = True

centro_x = screen.get_width() // 2




while running:
    for e in pygame.event.get():
        if e.type == QUIT:                    
            running = False

        if e.type == MOUSEMOTION:
            rect_player.center = e.pos

    offset = (rect_asteroid.x - rect_player.x, rect_asteroid.y - rect_player.y)
    if mask_player.overlap(mask_asteroid, offset) != None:
        print("Chocaron!!!")

    screen.fill(BLACK)

    screen.blit(asteroid, rect_asteroid)
    screen.blit(player, rect_player)

    pygame.display.flip()


pygame.quit()
exit() 