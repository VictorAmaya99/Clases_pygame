
import pygame
from pygame.locals import *
from config3 import *
from sprite_sheet import SpriteSheet

class Misil(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas) -> None:
        super().__init__(groups)       
        self.image = pygame.transform.scale(pygame.image.load("./FINAL_GAME/src/assets/images/Missile2.png").convert_alpha(), 
        (40,30))
        self.rect = self.image.get_rect(midbottom = coordenadas)
        self.speed_v =  5
   
        
    def update(self):        
        self.rect.y -= self.speed_v
        if self.rect.bottom < 0:
           self.kill()
 