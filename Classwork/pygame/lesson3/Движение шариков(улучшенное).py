import pygame
import random
pygame.init()
size = [600,600]
black=(   0,   0,   0)
white=( 255, 255, 255)
color =( 100, 55, 77)
color2 = ( 150, 65,255)
color3 = ( 150, 65,155)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Animations")
done = True
screen.fill(white)
clock=pygame.time.Clock()
x = 50
y = 50
x2 = 300
y2 = -100
x3 = 50
y3 = 50
koef = 1
koef2 = 1
koef3 = 1

while done:    
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done=False
       randchis = random.randint(50,550)
       #Движение оп оси X
       if x == 650:
              x = int(50)*(-1)             
       screen.fill(white)
       pygame.draw.circle(screen,color,(x,y),50,0)
       clock.tick(100)
       x = x+5*koef
       
       #Движение по оси Y
       if y2 == 650:
            y2 = int(50)*(-1)
            x2 = 50 + randchis
       pygame.draw.circle(screen,color2,(x2,y2),50,0)
       y2 = y2+5*koef2
       
       #Движение по оси Y (статичное)      
       if y3 > 600:
              koef3 = -1
       if y3 < -50:
              koef3 = 1
       pygame.draw.circle(screen,color3,(x3,y3),50,0)
       clock.tick(200)
       y3 = y3+5*koef3
       pygame.display.flip()
pygame.quit()
