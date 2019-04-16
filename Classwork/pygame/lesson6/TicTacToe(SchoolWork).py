import pygame
pygame.init()
size = [600,800]
black=(   0,   0,   0)
white=( 255, 255, 255)
red=( 255, 0, 0)
blue=( 0, 0, 255)
o = 'zero'
x = 'cross'
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
zanet = ['none',1,2,3,4,5,6,7,8,9]
steep = 0
while done:
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     done=False
              if event.type == pygame.MOUSEBUTTONDOWN:
                     if event.button == 1:
                            if event.pos[0] < 200 and event.pos[1] < 200:
                                   if  zanet[1] == 1:
                                          print('1. First cell')
                                          kv = 1
                                          pygame.draw.line(screen,red,[0,0],[200,200],3)
                                          pygame.draw.line(screen,red,[0,200],[200,0],3)
                                          zanet.insert(1, 'X')
                                   else:
                                          print('the move is already taken')
                            if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] < 200:
                                   print('2. Second cell')
                            if event.pos[0] < 600 and event.pos[0] > 400 and event.pos[1] < 200:
                                   print('3. Third cell')
                            if event.pos[0] < 200 and event.pos[1] > 200 and event.pos[1] < 400:
                                   print('4. Four cell')
                            if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] < 400 and event.pos[1] > 200:
                                   print('5. five cell')
                            if event.pos[0] < 600 and event.pos[0] > 400 and event.pos[1] > 200 and event.pos[1] < 400:
                                   print('6. Six cell')
                            if event.pos[0] < 200 and event.pos[0] > 0 and event.pos[1] > 400 and event.pos[1] < 600:
                                   print('7. Seven cell')
                            if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] > 400 and event.pos[1] < 600:
                                   print('8. Eight cell')
                            if event.pos[0] < 600 and event.pos[0] > 400 and event.pos[1] > 400 and event.pos[1] < 600:
                                   print('9. Nine cell')
       
pygame.quit()
