import pygame
pygame.init()
size = [600,800]
black=(   0,   0,   0)
white=( 255, 255, 255)
red=( 255, 0, 0)
blue=( 0, 0, 255)
o = 'Нолик'
x = 'Крестик'
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
pohodil = 1
zanet = [0,1,2,3,4,5,6,7,8,9]
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos) # Используеться для показа позиции курсора
                if event.pos[0] < 200 and event.pos[1] < 200:
                    #Проверка на наличии крестика или нолика в ячейкке
                    if zanet[1] == x or zanet[1] == o:
                        print('Ход был уже выполнен')
                    else:
                        #Проверка хода игрока
                        #0 - нолики
                        #1 - крестики
                        if pohodil == 0:
                            pygame.draw.circle(screen, blue, (100,100), 100, 3)
                            pohodil+=1
                            zanet.insert(1, o) #Замена цифры в списке ноликом
                        elif pohodil == 1:
                            pygame.draw.line(screen,red,[0,0],[200,200],3)
                            pygame.draw.line(screen,red,[0,200],[200,0],3)
                            pohodil += 1
                            zanet.insert(1, x) #Замена цифры в списке крестиком
                        pygame.display.flip()
                        print(zanet)
