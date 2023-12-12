# Se hizo una lista de diccionarios para manejar el rectangulo para hacer multiples bloques 

import pygame
from random import randint, randrange
from sys import exit
from config import *
from functions import *
from collisions import *
from pygame.locals import * 

pygame.init()

#Configuracion de pantalla principal: 
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

# Crear un reloj
clock = pygame.time.Clock()

# Evento personalizado del profesor:
EVENT_NEW_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NEW_COIN, 3000)

speed_x = 5
speed_y = 5

coin_size = 30

count = 0
cont_grande = 0

# Direccion movimiento teclas:(banderas)
move_up = False
move_down = False
move_right = False
move_left = False

font = pygame.font.SysFont(None, 48)

text = font.render(f"Coins: {count}", True, MAGENTA)
text_rect = text.get_rect()
text_rect.midtop = (WIDTH // 2 , 30)

# crear un bloque
block = generate_block(randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, 
                                 BLOCK_HEIGHT, RED, radius=25)
is_runnig = True

# crear lista de coins:
coins = []
for i in range(25):
    coins.append(generate_block(randint(0, WIDTH - coin_size), randint(0, HEIGHT - coin_size), coin_size, 
                                 coin_size, YELLOW, radius=coin_size//2))

while is_runnig:
    clock.tick(FPS)
    # Detectar los eventos: Esta es la parte unica para detectar eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            is_runnig = False
        
        if event.type == EVENT_NEW_COIN:
            coins.append(generate_block(randint(0, WIDTH - coin_size), randint(0, HEIGHT - coin_size), coin_size, 
                                 coin_size, MAGENTA, radius=coin_size//2))
            
        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                move_right = True
                move_left = False
            if event.key == K_LEFT or event.key == K_a:
                move_left = True
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = True
                move_down = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = True
                move_up = False
        
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False
            if event.key == K_ESCAPE:
                is_runnig = False

        if event.type == MOUSEBUTTONDOWN: 
            coins.append(generate_block(randint(0, WIDTH - coin_size), randint(0, HEIGHT - coin_size), 
                                coin_size, coin_size, LIGHT_PINK, radius=coin_size//2))

    # Actualizar los elementos:

    # Muevo el rectangulo de acuerdo a su direccion:
    if move_right and block["rect"].right <= (WIDTH - SPEED):
        #Derecha:
        block["rect"].left += SPEED

    if move_left and block["rect"].left >= (0 + SPEED):
        #Izquierda:
        block["rect"].left -= SPEED
       
    if move_up and block["rect"].top >= (0 + SPEED):
        #Arriba
        block["rect"].top -= SPEED

        #Abajo
    if move_down and block["rect"].bottom <= (HEIGHT - SPEED):
        block["rect"].top += SPEED
    
    for coin in coins [ : ]:
        if detectar_colision_cirC (coin["rect"], block["rect"]):
            coins.remove(coin)
            count += 1
            text = font.render(f"Coins: {count}", True, MAGENTA)
            text_rect = text.get_rect()
            text_rect.midtop = (WIDTH // 2 , 30)
            cont_grande = 30
    
    if cont_grande > 0:
        cont_grande -= 1
        block["rect"].width = BLOCK_WIDTH * 1.1
        block["rect"].height = BLOCK_HEIGHT * 1.1
        block["color"] = aleatory()
    else:
        block["rect"].width = BLOCK_WIDTH
        block["rect"].height = BLOCK_HEIGHT
        block["color"] = RED

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