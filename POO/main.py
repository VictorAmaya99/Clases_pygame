import pygame
import os
from random import *
from pygame.locals import *


images_dir = os.path.join(os.getcwd(), r"POO/assets/images")
sound_dir = os.path.join(os.getcwd(), r"POO/assets/sounds")

#uso de sprites:
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, size, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.image = pygame.transform.scale(pygame.image.load(image_path), size)
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
        self.laser_sound = pygame.mixer.Sound(os.path.join(sound_dir, "laser.mp3"))

    def update(self):
         self.rect.center = pygame.mouse.get_pos()
    
    def shoot(self, naves):
        self.laser_sound.play()
        pygame.sprite.spritecollide(self, naves, True) 


class Nave(Player):
    def __init__(self, image_path, size, pos_x, pos_y):
        super().__init__(image_path, size, pos_x, pos_y)

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
QTY_NAVE = 10       #QTY = cantidad
SIZE_NAVE = 50

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

fondo = pygame. transform. scale(pygame.image.load(os.path.join(images_dir, "background.png")), (WIDTH, HEIGHT))

naves_group = pygame.sprite.Group()
for nave in range(QTY_NAVE):
    nueva_nave = Nave(os.path.join(images_dir, "nave.png"), (SIZE_NAVE,SIZE_NAVE), 
                      randrange(SIZE_NAVE // 2, WIDTH - SIZE_NAVE //2), 
                      randrange(SIZE_NAVE // 2, HEIGHT - SIZE_NAVE //2))
    naves_group.add(nueva_nave)

player = Player(os.path.join(images_dir, "crosshair6.png"), (60, 60), 200, 200)
player_group = pygame.sprite.Group()
player_group.add(player)

pygame.mouse.set_visible(False)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == QUIT:
            running = False
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot(naves_group)

    screen.blit(fondo, (0,0))

    naves_group.draw(screen)

    player_group.update()
    player_group.draw(screen)

    pygame.display.flip()


pygame.quit()