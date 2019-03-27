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
screen.fill(green)
pygame.draw.rect(screen,black,[20,20,250,100],2)
pygame.draw.ellipse(screen,black,[20,20,250,100],2)
pygame.draw.circle(screen,black,(300,400),20,0)
pygame.draw.circle(screen,black,(300,400),40,1)
pygame.draw.polygon(screen,black,[[300,150],[0,200],[200,200]],5)
pygame.display.flip()
while done:    
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done=False

       
       #for y_offset in range(0,100,10):
           #pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],5)
           #pygame.display.flip()
           #clock.tick(20)

       clock.tick(20)
pygame.quit()
