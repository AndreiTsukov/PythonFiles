'''
import pygame
FPS = 120
W = 700 # ширина экрана
H = 300 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
STOP = "stop"
DOWN = " to the down"
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x = W // 2
y = H // 2
r = 50
motion = STOP
done = True
while done:
        sc.fill(WHITE)
        pygame.draw.circle(sc, BLUE, (x, y), r)
        pygame.display.update()
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
        clock.tick(FPS)
pygame.quit()
'''
import pygame
FPS = 120
W = 700 # ширина экрана
H = 300 # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
UP = "to the up"
STOP = "stop"
DOWN = " to the down"
pygame.init()
pilt = pygame.image.load('cars.png')
pilt2 = pygame.image.load('cars2.png')
pilt3 = pygame.image.load('cars3.png')
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x = 200
y = 200
samm = 10
motion = STOP
running = True
car = 0
while running:
        sc.fill([255, 255, 255])
        if car == 0:
                sc.blit(pilt, (x,y))
        elif car == 1:
                sc.blit(pilt2, (x,y))
        elif car == 2:
                sc.blit(pilt3, (x,y))
        pygame.display.flip()
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                        running = False
                elif i.type == pygame.KEYDOWN:
                        if i.key == pygame.K_UP:
                                motion = UP
                        elif i.key == pygame.K_DOWN:
                                motion = DOWN
                        elif i.key == pygame.K_LEFT:
                                motion = LEFT
                        elif i.key == pygame.K_RIGHT:
                                motion = RIGHT

                elif i.type == pygame.KEYUP:
                        if i.key in [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                                motion = STOP
        if motion == LEFT:
                x -= 3
                car = 1
        elif motion == RIGHT:
                x += 3
                car = 0
        elif motion == UP:
                y-=3
        elif motion == DOWN:
                y+=3
                car = 2
        clock.tick(FPS)
pygame.quit()
'''
import pygame
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill(WHITE)
pygame.display.update()
done = True

while done:
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                        done = False
        if i.type == pygame.MOUSEBUTTONDOWN:
                print(i.pos)
                if i.button == 1:
                        pygame.draw.circle(sc, RED, i.pos, 20)
                        pygame.display.update()
                elif i.button == 3:
                        pygame.draw.circle(sc, BLUE, i.pos, 20)
                        pygame.draw.rect(sc, GREEN, (i.pos[0]-10, i.pos[1]-10, 20,20))
                        pygame.display.update()
                elif i.button == 2:
                        sc.fill(WHITE)
                        pygame.display.update()
        elif i.type == pygame.MOUSEMOTION:
                x,y = i.pos
                pygame.draw.circle(sc, RED, i.pos, 20)
                pygame.display.update()


        pygame.time.delay(20)
pygame.quit()
'''
