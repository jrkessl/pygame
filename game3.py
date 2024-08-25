# sprites vieram de: https://pixelfrog-assets.itch.io/pixel-adventure-1/download/eyJleHBpcmVzIjoxNzI0NjA2NTAxLCJpZCI6NDkwNzk4fQ%3d%3d%2euaD59gwHdVnyJNcySfSZuSzubEU%3d
# tutorial de animação: https://www.geeksforgeeks.org/pygame-character-animation/

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
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 800
altura_jogador = 64 
largura_jogador = 64
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Joguinho nervoso")
 

class Enemy(pygame.sprite.Sprite):
    left = False 
    contadorVirada = 0

    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy1.png") # carrega a sprite do inimigo
        self.rect = self.image.get_rect() # cria a caixa de colisão 
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

        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
class Player(pygame.sprite.Sprite):
    animationCounter=0
    sprites_idle=[]
    sprites_run=[]
    velocidade_alteracao_sprite=0
    quantidade_sprites_idle=0
    quantidade_sprites_run=0
    sprite_atual=0
    indo_direita=True
    correndo=False

    # Inicialização do jogador 
    def __init__(self):
        super().__init__() 

        # Carrega as sprites idle
        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle1.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_idle.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle2.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle3.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle4.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle5.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle6.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle7.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle8.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle9.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle10.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/idle11.png")
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador))
        Player.sprites_idle.append(imagem)

        # Carrega as sprites run
        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run1.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run2.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run3.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run4.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run5.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run6.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run7.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run8.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run9.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run10.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run11.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        imagem = pygame.image.load("./pixel-adventure-1/Free/Main Characters/Virtual Guy/run12.png") # Carrega imagem 
        imagem = pygame.transform.scale(imagem, (altura_jogador, largura_jogador)) # Escalona a imagem 
        Player.sprites_run.append(imagem) # Guarda no array pra usar depois 

        self.image = Player.sprites_idle[0] # Define a sprite inicial do jogador
        self.rect = self.image.get_rect() # Cria a caixa de colisão
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # Posiciona o jogador

        Player.quantidade_sprites_idle = len(Player.sprites_idle) # Armazena a quantidade de sprites idle. 
        Player.quantidade_sprites_run = len(Player.sprites_run) # Armazena a quantidade de sprites run.
        
        # Definir a velocidade de mudança das sprites idle, em número de quadros que cada sprite é exibida; Elas precisam ser todas cicladas 1 vez por segundo, independentemente de quantas sprites sejam. 
        # Player.velocidade_alteracao_sprite = int(FPS / Player.quantidade_sprites_idle) # Cicla as imagens todas 1x por segundo, independentemente de quantas imagens o player tenha; 
        Player.velocidade_alteracao_sprite = int(FPS/15) # Cicla as imagens 15 vezes por segundo. A cada 66,6 milisegundos ou 4 quadros se a taxa for de 60 FPS. 
        # Player.velocidade_alteracao_sprite = 60 # Cicla a imagem uma vez por segundo apenas 
 
    def update(self):
        pressed_keys = pygame.key.get_pressed() # pega a tecla pressionada 
        
        if pressed_keys[K_LEFT]: # Se apertou tecla pra esquerda
            if self.rect.left > 0: # Se ainda não encostou na parede esquerda 
                self.rect.move_ip(-5, 0) # Move 5 posições pra esquerda 
                Player.indo_direita = False # Registra que agora ele está apontando pra esquerda 
                
                # Armazena que está correndo. Vai ser preciso pra escolher a sprite. Mas precisa ver se começou a correr agora. 
                if not Player.correndo: # Se não estava correndo até agora 
                    Player.sprite_atual = 0 # Zera o indicador de sprite, pois vamos começar pela primeira sprite do conjunto. 
                    Player.animationCounter = 0 # Zera o contador de animação, pois vamos trocar de sprite. 
                    Player.correndo = True 

        elif pressed_keys[K_RIGHT]: # Se apertou direita 
            if self.rect.right < SCREEN_WIDTH: # Se não está encostado na margem direita 
                self.rect.move_ip(5, 0) # Move 5 posições pra direita 
                Player.indo_direita = True # Registra que agora ele está apontando pra direita
                
                # Armazena que está correndo. Vai ser preciso pra escolher a sprite. Mas precisa ver se começou a correr agora. 
                if not Player.correndo: # Se não estava correndo até agora 
                    Player.sprite_atual = 0 # Zera o indicador de sprite, pois vamos começar pela primeira sprite do conjunto. 
                    Player.animationCounter = 0 # Zera o contador de animação, pois vamos trocar de sprite. 
                    Player.correndo = True 

        elif pressed_keys[K_UP]: # Se apertou tecla pra cima 
            if self.rect.top > 0:
                self.rect.move_ip(0, -5)
                
                # Armazena que está correndo. Vai ser preciso pra escolher a sprite. Mas precisa ver se começou a correr agora. 
                if not Player.correndo: # Se não estava correndo até agora 
                    Player.sprite_atual = 0 # Zera o indicador de sprite, pois vamos começar pela primeira sprite do conjunto. 
                    Player.animationCounter = 0 # Zera o contador de animação, pois vamos trocar de sprite. 
                    Player.correndo = True 
        
        elif pressed_keys[K_DOWN]: # se apertou pra baixo 
            if self.rect.bottom < SCREEN_HEIGHT: # se ainda não está na borda inferior 
                self.rect.move_ip(0, 5) # move 5 pixels pra baixo 
                
                # Armazena que está correndo. Vai ser preciso pra escolher a sprite. Mas precisa ver se começou a correr agora. 
                if not Player.correndo: # Se não estava correndo até agora 
                    Player.sprite_atual = 0 # Zera o indicador de sprite, pois vamos começar pela primeira sprite do conjunto. 
                    Player.animationCounter = 0 # Zera o contador de animação, pois vamos trocar de sprite. 
                    Player.correndo = True 
            
        else: # Se nenhuma tecla foi pressionada

            # Armazena que parou de correr. Vai ser preciso pra escolher a sprite. Mas precisa ver se parou de correr agora. 
            if Player.correndo: # Se estava correndo até agora 
                Player.sprite_atual = 0 # Zera o indicador de sprite, pois vamos começar pela primeira sprite do conjunto. 
                Player.animationCounter = 0 # Zera o contador de animação, pois vamos trocar de sprite. 
                Player.correndo = False # Registra que agora ele não está mais correndo. 

        # Animação do personagem: cicla a sprite, se for chegada a hora 
        # Este bloco só cicla a sprite (calcula se é chegada a hora de ciclar ela). A atribuição da imagem correta ao jogador vem depois. 
        if Player.animationCounter == Player.velocidade_alteracao_sprite: # Quando chegar na hora de trocar a sprite:
            Player.animationCounter = 0 # Reinicia o contador de animação.
            Player.sprite_atual += 1 # Move o indicador de próxima sprite pra frente. 
            if Player.sprite_atual == Player.quantidade_sprites_idle: # Se chegou no final da quantidade de sprites, volta para o início do vetor. 
                Player.sprite_atual = 0 
        Player.animationCounter += 1 # Incrementa em cada loop; Define o ritmo da animação. 

        # Atualiza a imagem do jogador 
        # Pra atualizar temos que saber pra que lado ele está olhando e vamos usar a sprite calculada no step anterior. 
        if Player.indo_direita: # Vê se o jogador está olhando pra direita ou esquerda 
            if Player.correndo: # Se ele está correndo
                self.image = Player.sprites_run[Player.sprite_atual] # Troca a sprite atual pela próxima da lista de sprites run.
            else:
                self.image = Player.sprites_idle[Player.sprite_atual] # Troca a sprite atual pela próxima da lista de sprites idle.
        else:
            if Player.correndo: # Se ele está correndo
                self.image = pygame.transform.flip(Player.sprites_run[Player.sprite_atual], True, False) # Troca a sprite atual pela próxima da lista de sprites run, mas flipada horizontalmente.
            else:
                self.image = pygame.transform.flip(Player.sprites_idle[Player.sprite_atual], True, False) # Troca a sprite atual pela próxima da lista de sprites idle, mas flipada horizontalmente.

        # if Player.indo_direita:
        #     print("indo direita")
        # else:
        #     print("indo esquerda")
 
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