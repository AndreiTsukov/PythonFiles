
import pygame
pygame.init()
size = [600,800]
black=(   0,   0,   0)
white=( 255, 255, 255)
red=( 255, 0, 0)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Cordinate sys")
done = True
screen.fill(white)
clock=pygame.time.Clock()
pygame.draw.line(screen,black,[0,0],[600,0],1)
pygame.draw.line(screen,black,[0,200],[600,200],1)
pygame.draw.line(screen,black,[0,400],[600,400],1)
pygame.draw.line(screen,black,[0,600],[600,600],1)
pygame.draw.line(screen,black,[200,0],[200,600],1)
pygame.draw.line(screen,black,[400,0],[400,600],1)
pygame.draw.line(screen,black,[600,0],[600,600],1)
pygame.display.flip()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    print(event.pos) #printed coursore positsion
                    if event.pos[0] < 200 and event.pos[1] < 200: #первая ячейка
                        pygame.draw.line(screen,red,[0,0],[200,200],3)
                        pygame.draw.line(screen,red,[0,200],[200,0],3)
                        pygame.display.flip()
                    if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] < 200 : #вторая ячейка
                        pygame.draw.line(screen,red,[200,0],[400,200],3)
                        pygame.draw.line(screen,red,[200,201],[400,0],3)
                        pygame.display.flip()
                    if event.pos[0] > 400 and event.pos[0] < 600 and event.pos[1] < 200 : #третья ячейка
                        pygame.draw.line(screen,red,[400,0],[600,200],3)
                        pygame.draw.line(screen,red,[600,0],[400,200],3)
                        pygame.display.flip()
                    if event.pos[0] < 400 and event.pos[1] < 400: #четвертая ячейка
                        pygame.draw.line(screen,red,[0,400],[200,200],3)
                        pygame.draw.line(screen,red,[0,200],[200,400],3)
                        pygame.display.flip()
                    
                   
                                
pygame.quit()


'''
if i.type == pygame.MOUSEBUTTONDOWN:
 if i.button == 1:
 pygame.draw.circle(sc, RED, i.pos, 20)
 pygame.display.update()
 elif i.button == 3:
 pygame.draw.circle(sc, BLUE, i.pos, 20)
 pygame.draw.rect(sc, GREEN, (i.pos[0]-10, i.pos[1]-10, 20,
20))
 pygame.display.update()
 elif i.button == 2:
 sc.fill(WHITE)
 pygame.display.update()

         for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    done=False
                    
              	elif event.type= pygame.MOUSEBUTTONDOWN:

              		if event.button == 1:

              			print(event.pos) 
 '''
