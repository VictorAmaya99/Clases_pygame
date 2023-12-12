
import pygame
from pygame.locals import *
from config3 import *
from sprite_sheet import SpriteSheet
from misil import Misil

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas) -> None:
        super().__init__(groups)

        self.sheet = SpriteSheet( pygame.image.load("./FINAL_GAME/src/assets/images/space_ship.png").convert_alpha(), 
                                 1,3, 64,64)
        self.animations =  self.sheet.get_animations_list()
        self.frame = 0
        self.image = self.animations[self.frame]
        self.rect = self.image.get_rect(center = coordenadas)
        self.speed = 0
        self.shoot_sound = pygame.mixer.Sound("./FINAL_GAME/src/assets/sounds/laser.wav")
        self.punch_sound = pygame.mixer.Sound("./FINAL_GAME/src/assets/sounds/punch.wav")

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.speed = -5
            self.frame = 2
        elif keys[K_RIGHT]:
            self.speed = 5
            self.frame = 1
        else:
            self.speed = 0
            self.frame = 0
        self.image = self.animations[self.frame]

        
    def move(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

    def update(self):        
        self.handle_events()
        self.move()

    def shoot(self, game):
        self.shoot_sound.play()
        Misil([game.all_sprites, game.player_shoots], self.rect.midtop)




