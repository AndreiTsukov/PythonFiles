import pygame
import random
import os

def animation_hero():
    global animCount
    screen.blit(bg,(0,0))
    if animCount + 1 >=30:
        animCount = 0
    if left:
        screen.blit(hero_left[animCount // 5],(x,y))
        animCount+=1
    elif right:
        screen.blit(hero_right[animCount // 5],(x,y))
        animCount+=1
    else:
        screen.blit(hero_default,(x,y))
    pygame.display.flip()
pygame.init()
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
path = os.path.dirname(__file__)
bg = pygame.image.load(os.path.join(path,'img/bg.jpg'))
##import img##
#right
hero_right = [
    pygame.image.load(os.path.join(path,'img/hero/right/1.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/2.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/3.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/4.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/5.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/6.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/7.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/8.png')),
    pygame.image.load(os.path.join(path,'img/hero/right/9.png'))
]
#left
hero_left = [
    pygame.image.load(os.path.join(path,'img/hero/left/1.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/2.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/3.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/4.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/5.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/6.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/7.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/8.png')),
    pygame.image.load(os.path.join(path,'img/hero/left/9.png'))
]
hero_default = pygame.image.load(os.path.join(path,'img/hero/left/1.png'))
done = True
x = 20
y = 479
animCount = 0
left = False
right = False
while done:
    screen.fill(white)
    screen.blit(bg,(0,0))
    screen.blit(hero_default,(x,y))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
        left = True
        right = False
    elif keys[pygame.K_RIGHT]:
        x += 3
        right = True
        left = False
    else:
        right = False
        left = False
        animCount = 0
    animation_hero()
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
