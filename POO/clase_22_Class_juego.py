import pygame
from pygame.locals import *
from config2 import *
from player import Player
from sprite_sheet import SpriteSheet
from player_jumper import PlayerJumper
from plataforma import Platform


class Game: 
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego con clases")
        pygame.display.set_icon(pygame.image.load("./POO/assets/images/boy_icon.png"))
        # Agrego al juego un grupo de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        sprite_sheet_player = SpriteSheet(pygame.image.load
                            ("./POO/assets/images/boy_sheet.png").convert_alpha(),
                            5, 4, WIDTH_PLAYER, HEIGHT_PLAYER, 
                            ["idle", "right", "left", "front", "back"])
        sprite_sheet_enemy = SpriteSheet(pygame.image.load
                            ("./POO/assets/images/squeletos.png").convert_alpha(),
                            4, 9, 64, 64, ["back", "left", "front", "right"])
        sprite_sheet_bebe = SpriteSheet(pygame.image.load
                            ("./POO/assets/images/baby.png").convert_alpha(),
                            4, 5, 50, 50, ["back", "left", "front", "right"])
        
        Platform([self.all_sprites, self.platforms], (300, 500, 200,50))
        Platform([self.all_sprites, self.platforms], (600, 450, 150,50))

        # Instancio un player y le paso el grupo donde va a pertenecer
        self.player = Player([self.all_sprites], sprite_sheet_player)
        self.enemy  = Player([self.all_sprites, self.enemies], sprite_sheet_enemy)
        self.baby  = PlayerJumper([self.all_sprites, self.enemies], sprite_sheet_bebe)

    def run(self): 
        running = True
        while running:
            self.clock.tick(FPS) 
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.baby.jump()

            self.draw()

            self.update() #Se actualiza el juego      
        
        self.close()

    def draw(self):
        self.screen.fill((200,200,200)) #Pintar la pantalla
    
        self.all_sprites.draw(self.screen)  

    def update(self):
 
        plataformas = pygame.sprite.spritecollide(self.baby, self.platforms, False)

        for plataforma in plataformas:
            
            if self.baby.rect.bottom >= plataforma.rect.top and self.baby.speed_v > 0:
                self.baby.rect.bottom = plataforma.rect.top
                self.baby.speed_v = 0

        self.all_sprites.update()
        pygame.display.flip() #Actualiza el juego

    def close(self):
        pygame.quit() #Cierra el juego

#para mostrar el juego se debe crear una instancia de la clase juego
#Se crea un objeto juego

if __name__ == "__main__": #Para que se ejecute solo en este archivo
                           #Es una forma de proteger el archivo y no se ejecute de otro lado
    game = Game()
    game.run() 
