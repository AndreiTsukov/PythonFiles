import pygame
import random
import os
#def animation_walk1(x,y):

pygame.init()
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = True
screen.fill(white)
pygame.display.flip()
working_dir = os.path.dirname(__file__) #используется , чтобы связать картинку с дерикторией
animation1 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/1.png')).convert()
animation2 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/2.png')).convert()
animation3 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/3.png')).convert()
animation4 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/4.png')).convert()
animation5 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/5.png')).convert()
animation6 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/6.png')).convert()
animation7 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/7.png')).convert()
animation8 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/8.png')).convert()
animation9 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/9.png')).convert()
animation10 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/10.png')).convert()
animation11 = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/right/11.png')).convert()
#left animation
animation2_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/2.png')).convert()
animation3_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/3.png')).convert()
animation4_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/4.png')).convert()
animation5_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/5.png')).convert()
animation6_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/6.png')).convert()
animation7_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/7.png')).convert()
animation8_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/8.png')).convert()
animation9_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/9.png')).convert()
animation10_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/10.png')).convert()
animation11_l = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/left/11.png')).convert()
STOP = 'stop'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'
UP = 'up'
bg = pygame.image.load(os.path.join(working_dir, 'img/animation_walk/bg.png')).convert()
x = 50 #дял кружка
y = 479 #для кружка
motion = STOP #Нужно для непрерывного движения
img = 0
while done:
    screen.fill(white)
    screen.blit(bg,(0,0))
    if img == 0:
        screen.blit(animation1,(x,y))
    #if img == 2:
        #animation_walk1(x,y)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
            elif i.key == pygame.K_UP:
                motion = UP
            elif i.key == pygame.K_DOWN:
                motion = DOWN
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                motion = STOP
                img = 0

    if motion == LEFT:
        x-=3
        list = [animation2_l,animation3_l,animation4_l,animation5_l,animation6_l,animation7_l,animation8_l,animation9_l,animation10_l,animation11_l]
        for i in list:
            screen.fill(white)
            screen.blit(bg,(0,0))
            screen.blit(i,(x,y))
            pygame.display.flip()
    elif motion == RIGHT:
        x += 3
        list = [animation1,animation2,animation3,animation4,animation5,animation6,animation7,animation8,animation9,animation10,animation11]
        for i in list:
            screen.fill(white)
            screen.blit(bg,(0,0))
            screen.blit(i,(x,y))
            pygame.display.flip()
    elif motion == UP:
        y-=3
    elif motion == DOWN:
        y+=3
    #Не дает выйти за рамки
    if y > 479:
        y-=3
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
