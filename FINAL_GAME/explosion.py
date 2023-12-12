from typing import Any
import pygame
from sprite_sheet import SpriteSheet

class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, coordenadas) -> None:
        super().__init__(groups)

        self.sheet = SpriteSheet( pygame.image.load("./FINAL_GAME/src/assets/images/exp_sheet.png").convert_alpha(), 
                                 4,4, 64,64)
        self.animations =  self.sheet.get_animations_list(scale=2)
        self.frame = 0
        self.image = self.animations[self.frame]
        self.rect = self.image.get_rect(center = coordenadas)
        self.last_update = pygame.time.get_ticks()
        self.speed_frame = 30 
        # self.sound = pygame.mixer.Sound("./FINAL_GAME/src/assets/sounds/explosion.wav")
        # self.sound.play()
        pygame.mixer.Sound("./FINAL_GAME/src/assets/sounds/explosion.wav").play()

    def update(self):        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.speed_frame:
            self.frame += 1
            if self.frame == len(self.animations):
                self.kill()
            else:
                self.image = self.animations[self.frame]
            
            self.last_update = current_time
        
       

 



