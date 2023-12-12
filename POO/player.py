import pygame
from pygame.locals import *
from config2 import *
from sprite_sheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet: SpriteSheet) -> None:
        super().__init__(groups)
        self.animations = sprite_sheet.get_animations_dict(scale=3)
        self.current_sprite = 0
        self.image = self.animations["right"][self.current_sprite]
        self.rect =self.image.get_rect(topleft = (0,0))
        self.speed = 5
        self.last_update = pygame.time.get_ticks()
        self.time_animation = 50
        
    def update(self):
        
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
        if keys[K_DOWN]:
            if self.rect.bottom <= HEIGHT:
                self.rect.y += self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["front"][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time
        if keys[K_UP]:
            if self.rect.y >= 0:
                self.rect.y -= self.speed
                current_time = pygame.time.get_ticks()
                if current_time - self.last_update >= self.time_animation:
                    self.current_sprite += 1
                    self.image = self.animations["back"][self.current_sprite]
                    if self.current_sprite == 3:
                        self.current_sprite = 0
                    self.last_update = current_time