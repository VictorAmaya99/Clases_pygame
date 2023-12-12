import pygame
from pygame.locals import *
from sprite_sheet import SpriteSheet
from player import Player
from config2 import *

class PlayerJumper(Player):
    def __init__(self, groups, sprite_sheet: SpriteSheet) -> None:
        super().__init__(groups, sprite_sheet)
        self.gravity = 1
        self.speed_v = 0
        self.jump_power = -20

    def update(self):

        self.speed_v += GRAVITY
        self.rect.y += self.speed_v

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.speed_v = 0
        
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["right"][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
        if keys[K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["left"][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
        
    def jump(self):
        self.speed_v = self.jump_power