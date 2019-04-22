import pygame
import random
def apple_red(x,y):
       pygame.draw.circle(screen,red,[x,y],20,0)
       pygame.draw.line(screen,black,[x+10,y-30],[x,y-15],5)
def apple_green(x,y):
       pygame.draw.circle(screen,green,[x,y],25,0)
pygame.init()
size = [800,600]
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = [0,0,0]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
done = True
screen.fill(white)
pygame.display.flip()
STOP = 'stop'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'
UP = 'up'
x = 50 #cyrcle
y = 50 #cyrcle
motion = STOP #Нужно для непрерывного движения
ountearv = random.randint(5,15)
ounad = []
radius = 45
ounwin = 0
win_str = ''
for i in range(ountearv):
       ounix = random.randint(50,750)
       ouniy = random.randint(50,550)
       ounad.append([ounix,ouniy])
while done:       
       screen.fill(white)
       apple_green(x,y)
       for oun in ounad:
              apple_red(oun[0],oun[1])    
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
       if motion == LEFT:
              x -= 3  
       elif motion == RIGHT:
             x += 3
       elif motion == UP:
              y-=3
       elif motion == DOWN:
              y+=3
       #Не дает выйти за рамки
              
       if x > 800:
              x = 0
       elif x < 0:
              x = 800
       elif y > 600:
              y = 0
       elif y < 0:
              y = 600
      
       for oun in ounad:
              if abs(oun[0] - x) < 45 and abs(oun[1] - y) < 45:
                     ounad.remove(oun)
                     ounwin += 1

       f1 = pygame.font.Font(None, 36)
       text1 = f1.render('Ты съел = '+str(ounwin)+str(win_str), 1, (180, 0, 0))
       screen.blit(text1,[0,550])
       if ounwin == ountearv:
              win_str = " , you win!"

              
       '''TEST ZONE'''
       #cyrcle motion
       print('x = ',x)
       #print('y = ',y)
       pygame.display.flip()
pygame.quit()
