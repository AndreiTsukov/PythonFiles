import pygame
#зарускаем программу
pygame.init()
#add colors
black=(   0,   0,   0)
white=( 255, 255, 255)
green=(   0, 255,   0)
red=( 255,   0,   0)
size = pygame.display.set_mode([600,600])
pygame.display.set_caption("car")
done = True
clock=pygame.time.Clock()
size.fill(white)
car = pygame.image.load('cars.png')
car2 = pygame.image.load('cars2.png')
x = 0
y = 0
koef=1
a = car
while done:    
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done=False
       if x > 500:
              koef = -1
              a = car2
       if x < 0:
              koef = 1
              a = car
       size.fill(white)
       size.blit(a,(x,y))
       x = x+5*koef
       clock.tick(100)
       pygame.display.flip()
pygame.quit()
