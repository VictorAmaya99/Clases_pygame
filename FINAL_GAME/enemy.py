
import pygame
from pygame.locals import *
from config3 import *
from sprite_sheet import SpriteSheet
from misil import Misil

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("./FINAL_GAME/src/assets/images/enemy_ship.png").convert_alpha()
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(center = coordenadas)
        self.speed = 5
        self.shoot_sound = pygame.mixer.Sound("./FINAL_GAME/src/assets/sounds/laser.wav")
       
    def update(self):        
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.speed = -5
            self.rect.y += 65
        elif self.rect.left < 0:
            self.speed = 5
            self.rect.y += 40
        elif self.rect.top > HEIGHT:
            self.kill()

    def shoot(self, game):
        self.shoot_sound.play()
        Misil([game.all_sprites, game.player_shoots], self.rect.midtop)




