import pygame
from config3 import *
from pygame.locals import *
from explosion import Explosion
from player import Player
from random import *
from enemy import Enemy 

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego final")
        self.background = pygame.transform.scale(pygame.image.load
                        ("./FINAL_GAME/src/assets/images/fondo.png"), 
                        (WIDTH, HEIGHT))
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.player_shoots = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.score = 0
        self.lives = 3

        self.player = Player([self.all_sprites], 
                             (WIDTH // 2, HEIGHT - 50))
        
        for _ in range(5):
            Enemy([self.all_sprites, self.enemies], (randrange(50, WIDTH - 50), 35))

    def detect_collisions(self):
        hits = pygame.sprite.groupcollide(self.enemies, self.player_shoots, True, True)

        for hit in hits:
            self.score += 10
            Explosion([self.all_sprites], hit.rect.center)
            print(self.score)

   
        hits = pygame.sprite.spritecollide(self.player, self.enemies, True)

        for hit in hits:
            self.lives -= 1
            self.player.punch_sound.play()
            Explosion([self.all_sprites], hit.rect.center)
            print(self.lives)
            if self.lives == 0:
                self.player.kill()
           

    def run(self):
        while self.running:  
            self.handle_events()
            self.update()
            self.detect_collisions()
            self.render()
            self.clock.tick(FPS)
        self.close()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.shoot(self)
    
    def update(self):
        self.all_sprites.update()

    def render(self):  #render donde va los blits y los draws
        #self.screen.fill((0,0,0))
        self.screen.blit(self.background, (0,0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
      
   
    def close(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()







