import pygame
import time
pygame.init()
size = [600,800]
black=(   0,   0,   0)
white=( 255, 255, 255)
red=( 255, 0, 0)
blue=( 0, 0, 255)
o = 'O'
x = 'X'
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Cordinate sys")
done = True
screen.fill(white)
clock=pygame.time.Clock()
crosswin = pygame.image.load('crosswin.jpg')
zeroswin = pygame.image.load('zeroswin.jpg')
draw = pygame.image.load('draw.jpg')
pygame.draw.line(screen,black,[0,0],[600,0],1)
pygame.draw.line(screen,black,[0,200],[600,200],1)
pygame.draw.line(screen,black,[0,400],[600,400],1)
pygame.draw.line(screen,black,[0,600],[600,600],1)
pygame.draw.line(screen,black,[200,0],[200,600],1)
pygame.draw.line(screen,black,[400,0],[400,600],1)
pygame.draw.line(screen,black,[600,0],[600,600],1)
pygame.display.flip()
pohodil = 1
steep = 0
win = 0
zanet = ['none',1,2,3,4,5,6,7,8,9]
def winner():
    if zanet[1] == zanet[2] == zanet[3]:
        return True
    if zanet[4] == zanet[5] == zanet[6]:
        return True
    if zanet[7] == zanet[8] == zanet[9]:
        return True
    if zanet[1] == zanet[4] == zanet[7]:
        return True
    if zanet[2] == zanet[5] == zanet[8]:
        return True
    if zanet[3] == zanet[6] == zanet[9]:
        whowins()
    if zanet[1] == zanet[5] == zanet[9]:
        return True
    if zanet[3] == zanet[5] == zanet[7]:
        return True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] < 200 and event.pos[1] < 200: #1
                    #Проверка на наличии крестика или нолика в ячейкке
                    if zanet[1] == x or zanet[1] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (100,100), 100, 3)
                            pohodil+=1
                            zanet[1] = 'O' #Замена цифры в списке ноликом
                            steep += 1
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[0,0],[200,200],3)
                            pygame.draw.line(screen,red,[0,200],[200,0],3)
                            pohodil -= 1
                            steep += 1
                            zanet[1] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] < 200: #2
                    #Проверка на наличии крестика или нолика в ячейкке
                    if zanet[2] == x or zanet[2] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (300,100), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[2] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[200,0],[400,200],3)
                            pygame.draw.line(screen,red,[400,0],[200,200],3)
                            pohodil -= 1
                            steep += 1
                            zanet[2] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 600 and event.pos[0] > 400 and event.pos[1] < 200: #3
                    #Проверка на наличии крестика или нолика в ячейкке
                    if zanet[3] == x or zanet[3] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (500,100), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[3] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[400,0],[600,200],3)
                            pygame.draw.line(screen,red,[600,0],[400,200],3)
                            pohodil -= 1
                            steep += 1
                            zanet[3] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 200 and event.pos[1] > 200 and event.pos[1] < 400: #4
                    if zanet[4] == x or zanet[4] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (100,300), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[4] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[0,200],[200,400],3)
                            pygame.draw.line(screen,red,[200,200],[0,400],3)
                            pohodil -= 1
                            steep += 1
                            zanet[4] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] < 400 and event.pos[1] > 200: #5
                    if zanet[5] == x or zanet[5] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (300,300), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[5] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[200,200],[400,400],3)
                            pygame.draw.line(screen,red,[400,200],[200,400],3)
                            pohodil -= 1
                            steep += 1
                            zanet[5] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 600 and event.pos[0] > 400 and event.pos[1] > 200 and event.pos[1] < 400: #6
                    if zanet[6] == x or zanet[6] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (500,300), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[6] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[400,200],[600,400],3)
                            pygame.draw.line(screen,red,[600,200],[400,400],3)
                            pohodil -= 1
                            steep += 1
                            zanet[6] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 200 and event.pos[0] > 0 and event.pos[1] > 400 and event.pos[1] < 600: #7
                    if zanet[7] == x or zanet[7] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (100,500), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[7] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[0,400],[200,600],3)
                            pygame.draw.line(screen,red,[200,400],[0,600],3)
                            pohodil -= 1
                            steep += 1
                            zanet[7] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 400 and event.pos[0] > 200 and event.pos[1] > 400 and event.pos[1] < 600: #8
                    if zanet[8] == x or zanet[8] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (300,500), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[8] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[200,400],[400,600],3)
                            pygame.draw.line(screen,red,[400,400],[200,600],3)
                            pohodil -= 1
                            steep += 1
                            zanet[8] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if event.pos[0] < 600 and event.pos[0] > 400 and event.pos[1] > 400 and event.pos[1] < 600: #9
                    if zanet[9] == x or zanet[9] == o:
                        print('the move is already taken')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (500,500), 100, 3)
                            pohodil+=1
                            steep += 1
                            zanet[9] = 'O' #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[400,400],[600,600],3)
                            pygame.draw.line(screen,red,[600,400],[400,600],3)
                            pohodil -= 1
                            steep += 1
                            zanet[9] = 'X' #Замена цифры в списке крестиком
                        print(zanet)
                if winner() == True:
                    if pohodil == 0:
                        screen.blit(crosswin, (0,601))
                        print("crosswin")
                    else:
                        screen.blit(zeroswin, (0,601))
                        print("zeroswin")
                elif steep == 9:
                    if winner() == True:
                        if pohodil == 0:
                            screen.blit(crosswin, (0,601))
                            print("crosswin")
                        else:
                            screen.blit(zeroswin, (0,600))
                            print("zeroswin")
                    else:
                        screen.blit(draw, (0,601))
                        print("draw")
pygame.quit()
