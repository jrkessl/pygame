import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 

class Enemy(pygame.sprite.Sprite):
    left = False 
    contadorVirada = 0

    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
    def move(self):
        Enemy.contadorVirada = Enemy.contadorVirada + 1 
        random_number = random.randint(0, 1) 
        # print(f"random_number={random_number}")

        if(Enemy.contadorVirada > 40):
            if (random_number == 0):
                Enemy.left = True
            else:
                Enemy.left = False
            Enemy.contadorVirada = 0
            

        # print(f"Enemy.left={Enemy.left}")
        if (Enemy.left):
            self.rect.move_ip(-1,5)
        else:
            self.rect.move_ip(1,5)

        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed() # pega a tecla pressionada 
         
        
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

        if pressed_keys[K_UP]:
            if self.rect.top > 0:
                self.rect.move_ip(0, -5)
        
        if pressed_keys[K_DOWN]: # se apertou pra baixo 
            if self.rect.bottom < SCREEN_HEIGHT: # se ainda não está na borda inferior 
                self.rect.move_ip(0, 5) # move 5 pixels pra baixo 
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()

    # detecção de colisão
    if pygame.sprite.spritecollideany(P1, enemies): # detecta colisão 
        new_image = pygame.image.load("explodido-generico.png") # carrega imagem 
        P1.image = new_image # seta nova imagem no player e enemy 
        E1.image = new_image
        DISPLAYSURF.blit(E1.image, E1.rect) # "renderiza" a nova imagem no player e enemy 
        DISPLAYSURF.blit(P1.image, P1.rect)
        pygame.display.update() # atualiza a tela 
        # for entity in all_sprites: # remove todas as sprites da tela 
        #     entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()     
     
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)