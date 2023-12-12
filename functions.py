import pygame
from random import randrange, randint
from config import *
from collisions import *
from pygame.locals import * 
from utils import *


def color_random(lista_colores): #Devuelve los colores que estan en la lista
    size = len(lista_colores)
    index = randrange(size)
    return lista_colores[index]

def aleatory(): #Devuelve colores aleatorios que elige el programa
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return (r, g, b) 
 
#Funcion que crea un bloque:
def generate_block(imagen = None, left=0, top=0, width=40, height=40, color=(255,255,255), dir=3, edge=0, radius=-1, speed_x=5, speed_y=5):
    rec = pygame.Rect(left, top, width, height)
    if imagen:
        imagen = pygame.transform.scale(imagen, (width, height))
    return {"rect": rec, "color": color, "dir": dir, "edge": edge, "radius": radius, "speed_x": speed_x, "speed_y":speed_y, "imagen": imagen}

coins = []
def handler_new_coin():
    coins.append(generate_block(None, randint(0, WIDTH - coin_size), randint(0, HEIGHT - coin_size), coin_size, 
                                 coin_size, YELLOW, radius=coin_size//2))
    
# def load_coins_list(coins, cantidad, imagen = None):
#     for i in range(cantidad):
#         coin_size = randint(size_min_coin, size_max_coin)
#         coins.append(generate_block(imagen, randint(0, WIDTH - coin_size), 
#                                     randint(- HEIGHT, - coin_size), coin_size, 
#                                     coin_size, YELLOW, radius=coin_size//2))

def load_coins_list(coins, cantidad, imagen = None):
    for i in range(cantidad): 
        coin_size = randint(size_min_coin, size_max_coin)
        speed_coin = randint(speed_min_coin, speed_max_coin)
        coins.append(generate_block(imagen, randint(0, WIDTH - coin_size), 
                                    randint(- HEIGHT, - coin_size), coin_size, 
                                    coin_size, YELLOW, speed_y = speed_coin, radius=coin_size//2))
        

def drawing_asteroids(superficie, coins):
    for coin in coins:
        if coin["imagen"]:
           superficie.blit(coin["imagen"], coin["rect"])
        else:
           pygame.draw.rect(superficie, coin["color"], coin["rect"], coin["edge"], coin["radius"]) 

def end():
    pygame.quit()
    exit()

def click_pause():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                end()        
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    end()
                return None
            
def click_pause_user(rect_1:pygame.Rect):
    while True:
        crear_boton(screen, rect_1, "Comenzar", BLUE, GREEN)
        pygame.display.flip() 
        for e in pygame.event.get():
            if e.type == QUIT:
                end()        
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    end()
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if rect_1.collidepoint(e.pos):
                        return None
            
def show_text(surface, text, font, coordinates, fond_color, background_color=BLACK):
    sup_text = font.render(text, True, fond_color, background_color)
    text_rect = sup_text.get_rect()
    text_rect.center = coordinates
    surface.blit(sup_text, text_rect)
    # pygame.display.flip()


