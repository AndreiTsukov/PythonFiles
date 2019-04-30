import pygame
#зарускаем программу
pygame.init()
#add colors
black=(   0,   0,   0)
white=( 255, 255, 255)
green=(   0, 255,   0)
red=( 255,   0,   0)
size = [700,700]
sc=pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")
done = True
clock=pygame.time.Clock()
sc = pygame.display.set_mode((300, 200))
surf = pygame.Surface((200, 150))
surf.fill((255, 255, 255))
surf.set_alpha(200)
# сначала на главной поверхности рисуется зеленый прямоуг.
pygame.draw.rect(sc, (0, 255, 0), (0, 80, 300, 40))
# затем другая поверхность,
# она будет поверх прямоугольника
sc.blit(surf, (50, 25))
pygame.display.update()
while done:
       for event in pygame.event.get():
               if event.type == pygame.QUIT:
                     done=False
       clock.tick(20)
pygame.quit()
