import pygame
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
y2 = 0
x3 = 0
y3 = 0
koef = 1
koef2 = 1
koef3 = 1

while done:    
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done=False
       
       if x > 600:
              koef = -1
       if x < 0:
              koef = 1
       screen.fill(white)
       pygame.draw.circle(screen,color,(x,y),50,0)
       clock.tick(100)
       x = x+5*koef

       if y2 > 600:
              koef2 = -1
       if y2 < 0:
              koef2 = 1
       pygame.draw.circle(screen,color2,(x2,y2),50,0)
       clock.tick(100)
       y2 = y2+5*koef2
       
       if y3 > 600 and x3 > 600:
              koef3 = -1
       if y3 < 0 and x3 < 0:
              koef3 = 1
       pygame.draw.circle(screen,color3,(x3,y3),50,0)
       clock.tick(100)
       y3 = y3+5*koef3
       x3 = x3+5*koef3
       pygame.display.flip()
       
pygame.quit()
