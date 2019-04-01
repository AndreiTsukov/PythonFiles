import pygame,sys
import random
#зарускаем программу
pygame.init()
#add colors
black=(   0,   0,   0)
white=( 255, 255, 255)
green=(   0, 255,   0)
red=( 255,   0,   0)
colorz=(250, 175, 1)
colorz1=(153, 0, 0)
colorz2=(102, 51, 0)
colorz3=(255, 102, 0)
size = [800,600]
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")
done = True
clock=pygame.time.Clock()
screen.fill(white)
for y in range(1,50):
       color1= random.randint(0,255)
       color2= random.randint(0,255)
       color3= random.randint(0,255)
       color = (color1,color2,color3)
       pygame.draw.circle(screen,color,(random.randint(0,800),random.randint(0,600)),random.randint(5,30),2)
       pygame.display.flip()
pygame.draw.circle(screen,colorz,(400,300),100,0)
pygame.draw.circle(screen,colorz,(400,500),150,0)
pygame.draw.circle(screen,colorz,(400,170),50,0)
pygame.draw.line(screen,black,[300,300],[110,500],5)
pygame.draw.line(screen,black,[500,300],[600,200],5)
pygame.draw.line(screen,colorz1,[600,150],[600,600],7)
pygame.draw.polygon(screen,black,[[400,50],[450,125],[350,125]],0)
pygame.draw.circle(screen,red,(600,150),50,0)
pygame.draw.circle(screen,black,(380,170),5,0)
pygame.draw.circle(screen,black,(420,170),5,0)
pygame.draw.polygon(screen,colorz3,[[400,200],[415,170],[385,170]],0)
pygame.display.flip()
while done:    
       for event in pygame.event.get(): 
               if event.type == pygame.QUIT: 
                     done=False
       clock.tick(20)
pygame.quit()
