import pygame, time, sys
from pygame.locals import *
import random

pygame.init()

FPS = 30
framesPerSec = pygame.time.Clock()

black = (0,0,0)
red = (255, 0, 0)

window = pygame.display.set_mode((500,600))
window.fill(black)
pygame.display.set_caption("Processando")

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

from pygame import mixer
mixer.init()
mixer.music.load("eletrorobo.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("papelcarai.png")
        self.surf = pygame.Surface((40,40))
        self.rect = self.surf.get_rect(center = (random.randint(40,460), (random.randint(-100,0))))

    def move(self, score):
        self.rect.move_ip(0,10)
        if(self.rect.bottom > 600):
            self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
            score += 1

        return score
               
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("motherchip.png")
        self.surf = pygame.Surface((100,150))
        self.rect = self.surf.get_rect(center = (250, 525))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressedKeys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(-10, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(10, 0)

class Background():
    def __init__(self):
        self.backgroundImage = pygame.image.load("xp2.jpg")
        self.rectBGimage = self.backgroundImage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = 0
    

    def render(self):
        window.blit(self.backgroundImage,(self.bgX1, self.bgY1))
        window.blit(self.backgroundImage,(self.bgX2, self.bgY2))



background = Background()


    

        

P1 = Player()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()

enemyGroup = pygame.sprite.Group()
enemyGroup.add(E1)
enemyGroup.add(E2)
enemyGroup.add(E3)

font = pygame.font.SysFont("Verdana", 52)
gameOver = font.render("Bugou!", True, black)

score = 0

while True:
    scoreRender = font.render("Score: " +str(score), True, red)
    background.render()
    window.blit(scoreRender, (0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if pygame.sprite.spritecollideany(P1, enemyGroup):
        window.fill(red)
        window.blit(gameOver, (150,300))
        pygame.display.update()
        time.sleep(4)
        pygame.quit()

    for enemy in enemyGroup:
        score = enemy.move(score)
        enemy.draw(window)

    P1.update()
    P1.draw(window)

    pygame.display.update()
    framesPerSec.tick(FPS)














    
            
            

    














    
        
    
