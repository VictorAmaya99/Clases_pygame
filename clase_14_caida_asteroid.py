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

# Set sonidos:
coin_sound = pygame.mixer.Sound("./src/assets/coin2.mp3")
game_over_sound = pygame.mixer.Sound("./src/assets/game-over.mp3")
end_level_sound = pygame.mixer.Sound("./src/assets/ganar.mp3")

#para cargar una musica de fondo:
pygame.mixer.music.load("./src/assets/game-thrones-violin.mp3")
#pygame.mixer.music.play(-1) #play tiene tres parametros (-1 es infinito), 
pygame.mixer.music.set_volume(0.1) #Establece el volumen deseado
playing_music = True

#cargar imagenes:
image_player = pygame.image.load("./src/assets/ovni.png")
image_asteroid = pygame.image.load("./src/assets/asteroide1.png")
image_asteroid2 = pygame.image.load("./src/assets/asteroide2.png")
background = pygame.transform.scale(pygame.image.load("./src/assets/fondo.jpg"), SCREEN_SIZE)

# Evento personalizado del profesor:
EVENT_NEW_COIN = pygame.USEREVENT + 1

pygame.time.set_timer(EVENT_NEW_COIN, 3000)

speed_x = 5
speed_y = 5

coin_size = 30

max_count = 0
cont_grande = 0
count_coins = 20

trick_reverse = False
trick_slow = False

# Direccion movimiento teclas:(banderas)
move_up = False
move_down = False
move_right = False
move_left = False
count = 0

laser = None

# set fuente
font = pygame.font.SysFont(None, 48)

text = font.render(f"Coins: {count}", True, MAGENTA)
text_rect = text.get_rect()
text_rect.midtop = (WIDTH // 2 , 30)

# crear un bloque
block = generate_block(image_player, randint(0, WIDTH - BLOCK_WIDTH), randint(0, HEIGHT - BLOCK_HEIGHT), BLOCK_WIDTH, 
                                 BLOCK_HEIGHT, RED, radius=25)
# crear lista de coins:
# coins = []
# load_coins_list(coins, count_coins, image_asteroid)



while True:

    #Pantalla inicio:
    screen.fill(BLACK)
    show_text(screen, "Asteroids", font, (WIDTH // 2, 20), BLUE)
    show_text(screen, "Presione un tecla para comenzar...", font, (WIDTH // 2, HEIGHT // 2), WHITE)
    pygame.display.flip()
    click_pause()

    #Inicializacion juego:
    pygame.mouse.set_visible(False)    
    count = 0
    text = font.render(f"Coins: {count}", True, MAGENTA)
    text_rect = text.get_rect()
    text_rect.midtop = (WIDTH // 2 , 30)
    game_time = FPS * 30
    is_runnig = True
    pygame.mixer.music.play(-1) #play tiene tres parametros (-1 es infinito)

    coins = []
    load_coins_list(coins, count_coins, image_asteroid)    

    while is_runnig:
        clock.tick(FPS)
        game_time -= 1 
        # Detectar los eventos: Esta es la parte unica para detectar eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                is_runnig = False
            
            if event.type == EVENT_NEW_COIN:
                pass
                #handler_new_coin()
                
            if event.type == KEYDOWN:
                if event.key == K_f:
                    if not laser:
                        midtop = block["rect"].midtop
                        laser_width, laser_height = size_laser
                        laser = generate_block(None, midtop[0] - laser_width // 2, midtop[1] - laser_height, 
                                               laser_width, laser_height, RED, speed_y= speed_laser)
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

                #Para pausar la musica:
                if event.key == K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music

                #Pausar el juego:
                if event.key == K_p:
                    if playing_music:
                        pygame.mixer.music.pause()
                    show_text(screen, "Pausa", font, CENTER, RED, BLACK)
                    pygame.display.flip()
                    click_pause()    
                    if playing_music:
                        pygame.mixer.music.unpause()

                if event.key == K_r:
                    trick_reverse = True
                
                if event.key == K_l:
                      trick_slow = True
                    
            
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
                
                if event.key == K_r:
                    trick_reverse = False
                
                if event.key == K_l:
                    trick_slow = False                  

            if event.type == MOUSEBUTTONDOWN: 
                #coins.append(generate_block(event.pos[0] - coin_size//2, event.pos[1] - coin_size//2,  coin_size, coin_size, LIGHT_PINK, radius=coin_size//2))
                if event.button == 1:#solo entra cuando hace click con el boton derecho
                    new_coin = generate_block(None, event.pos[0], event.pos[1], coin_size, coin_size, LIGHT_PINK, radius=coin_size//2)
                    new_coin["rect"].left -= coin_size // 2
                    new_coin["rect"].top -= coin_size // 2
                    coins.append(new_coin)
                
                if event.button == 3:
                    block["rect"].center = CENTER

            if event.type == MOUSEMOTION:
                block["rect"].center = (event.pos[0], event.pos[1])


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

        pygame.mouse.set_pos(block["rect"].centerx, block["rect"].centery)

        #Movemos los asteroides:
        for coin in coins: #Los coins en este codigo serian los asteroides
            #if trick_reverse != True and trick_slow != True:
            #if trick_reverse == False and trick_slow == False: 
            if not trick_reverse and not trick_slow:      
                coin["rect"].move_ip(0, coin["speed_y"]) #move_ip significa in place, como se desplaza tanto a la derecha o la izquiera, arriba o abajo
            elif trick_reverse:
                coin["rect"].move_ip(0, -coin["speed_y"])
            elif trick_slow:
                coin["rect"].move_ip(0, 1)
        
        #Muevo el laser:
        if laser:
            if laser["rect"].bottom >= 0:
                laser["rect"].move_ip(0, -laser["speed_y"])
            else:
                laser = None

        # for coin in coins:
        #     if coin["rect"].top > HEIGHT:
        #         coin["rect"].move_ip(0, -(HEIGHT + coin["rect"].height))

        for coin in coins[:]:
            if coin["rect"].top > HEIGHT:
                coins.remove(coin)
        
        for coin in coins [ : ]:
            if detectar_colision_cirC (coin["rect"], block["rect"]):
                coins.remove(coin)

                is_runnig = False

                if playing_music:
                    coin_sound.play()
            
            if len(coins) == 0:
                load_coins_list(coins, count_coins, image_asteroid2)
                end_level_sound.play()
        
        if laser: 
            colision = False
            for coin in coins [ : ]:
                if detectar_colision_cirC (coin["rect"], laser["rect"]):
                    coins.remove(coin)
                    count += 1
                    text = font.render(f"Coins: {count}", True, MAGENTA)
                    text_rect = text.get_rect()
                    text_rect.midtop = (WIDTH // 2 , 30)
                    cont_grande = 10
                    colision = True
                    if playing_music:
                        coin_sound.play()
                
                if len(coins) == 0:
                    load_coins_list(coins, count_coins, image_asteroid2)
                    end_level_sound.play()
            
            if colision == True:
                laser = None
            
        if cont_grande > 0:
            cont_grande -= 1
            block["rect"].width = BLOCK_WIDTH * 1.1
            block["rect"].height = BLOCK_HEIGHT * 1.1
            block["color"] = aleatory()
        else:
            block["rect"].width = BLOCK_WIDTH
            block["rect"].height = BLOCK_HEIGHT
            block["color"] = RED

        #Blitear imagen de fondo:
        screen.blit(background, ORIGIN)
        
        # Dibujar pantalla:
        #screen.fill(BLACK) # La pantalla se pinta cada vez que hay una interaccion, se pinta primero la pared y despues el rectangulo

        drawing_asteroids(screen, coins)

        # Dibujo el laser
        if laser:
            pygame.draw.rect(screen, laser["color"], laser["rect"])

        #Blitear imagen: 
        screen.blit(block["imagen"], block["rect"])

        # Blitear para poner el texto:
        screen.blit(text, text_rect)

        pygame.display.flip()

        if game_time == 0:
            is_runnig = False

    if count > max_count:
        max_count = count

    screen.fill(BLACK)
    pygame.mixer.music.stop()
    game_over_sound.play()
    show_text(screen, "Game over", font, (WIDTH // 2, 20), BLUE)
    show_text(screen, "Presione un tecla para comenzar...", font, (WIDTH // 2, HEIGHT // 2), WHITE)
    show_text(screen, f"Max score: {max_count}", font, (WIDTH // 2, HEIGHT - 30), YELLOW)
    pygame.display.flip()
    click_pause()
    
end()