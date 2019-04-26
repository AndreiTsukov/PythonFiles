import pygame
import random
import os
pygame.init()
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
done = True
while done:
    screen.fill(white)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            done = False
    pygame.display.flip()
pygame.quit()
