import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
FPS = 60

CUSTOM = (200, 200, 200)
BLACK = (0,0,0)

def get_image(hoja_sprites, frame, width, height, escala = 1, color = (0,0,0)):
    imagen = pygame.Surface((width,height))
    hoja_sprites.set_clip((frame * width,0,width,height))
    frame = hoja_sprites.subsurface(hoja_sprites.get_clip())
    imagen.set_colorkey(color)
    imagen.blit(frame, (0,0))
    imagen = pygame.transform.scale(imagen, (width * escala, height * escala))
    return imagen

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

hoja_sprites = pygame.image.load("./POO/assets/images/doux.png")
#La imagen se tiene que recortar. recortar una superficie y blitearla
#En la surface negra

ultima_actualizacion = pygame.time.get_ticks()
frame = 0
cant_frames = 20

#imagen = pygame.Surface((24,24))

#Lo primero que hay que hacer es extraer un pedazo de superficie. Hay dos manera:
#Primer metodo:
#hoja_sprites.set_clip((0,0,24,24)) #set_clip, corta una parte de la superficie donde se va a concentrar
#una vez que se hace el set, se hace el get, para sacar un pedazo de la superficie principal
#frame = hoja_sprites.subsurface(hoja_sprites.get_clip())#Es la parte recortada que se guarda en la variable frame
# imagen.blit(frame, (0,0))

#imagen.set_colorkey(BLACK)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
          if event.type == QUIT:
               running = False

    player = get_image(hoja_sprites, frame, 24, 24, 3)
    tiempo_actual = pygame.time.get_ticks() 
    if tiempo_actual - ultima_actualizacion >= 100:
        frame += 1
        if frame >= cant_frames:
            frame = 0
        ultima_actualizacion = tiempo_actual
    
    screen.fill(CUSTOM)
    screen.blit(player, (0,24))

    screen.blit(hoja_sprites, (0,0))

    


    pygame.display.update()

pygame.quit()