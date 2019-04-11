import pygame
import random
#зарускаем программу
class Ball():
    # --- Атрибуты класса ---
    # Ball position
    x=0
    y=0
    # Ball's vector
    change_x=0
    change_y=0
    # Ball size
    size=50
    # Ball color
    color=[255,255,255]
    # --- Методы класса ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y   
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )
pygame.init()
#add colors
FPS = 120
black=(   0,   0,   0)
white=( 255, 255, 255)
green=(   0, 255,   0)
red=( 255,   0,   0)
size = [600,400]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")
done = True
clock=pygame.time.Clock()
screen.fill(white)
theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [60,50,155]

while done:    
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done=False
       screen.fill(white)
       if theBall.x > 550 or theBall.x < 50:
               theBall.change_x = theBall.change_x * -1
               print('x = ',theBall.change_x)
       if theBall.y > 350 or theBall.y < 50:
               theBall.change_y = theBall.change_y * -1
               print('y = ',theBall.change_y)
       theBall.move()
       theBall.draw(screen)
       pygame.display.flip()
       clock.tick(FPS)
pygame.quit()
