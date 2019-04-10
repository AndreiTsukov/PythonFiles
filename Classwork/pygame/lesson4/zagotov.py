import pygame
#зарускаем программу
pygame.init()
#add colors
white=( 255, 255, 255)
red=( 255,   0,   0)
size = [700,700]
FPS = 100
x = 50
y = 50
r = 50
STOP = 'stop'
RIGHT = "to the right"
LEFT = "to the left"
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Key - game")
clock=pygame.time.Clock()
motion = STOP
done = True
while done:
       screen.fill(white)
       pygame.draw.circle(screen,red,(x,y),r)
       pygame.display.update()
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done = False
               elif event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_LEFT:
                             x-=10
                      if event.key == pygame.K_RIGHT:
                             x+=10
                      if event.key == pygame.K_DOWN:
                             y+=10
                      if event.key == pygame.K_UP:
                             y-=10
               elif event.type == pygame.KEYUP:
                      if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                             motion = STOP
       if motion == LEFT:
              x-=10
       elif motion == RIGHT:
              x+=10
       clock.tick(FPS)
pygame.quit()
