import pygame
#зарускаем программу
pygame.init()
#add colors
black=(   0,   0,   0)
white=( 255, 255, 255)
green=(   0, 255,   0)
red=( 255,   0,   0)
size = [700,700]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")
done = True
clock=pygame.time.Clock()

surf = pygame.Surface((200,150))
surf.fill(white)
screen.blit(surf, (50,25))
pygame.display.flip()
while done:
       for event in pygame.event.get():
               if event.type == pygame.QUIT:
                     done=False
       clock.tick(20)
pygame.quit()
