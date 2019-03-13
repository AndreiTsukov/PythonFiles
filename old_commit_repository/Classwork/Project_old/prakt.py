import random
prav = 0
nprav = 0
raz = int(input('Количество заданий для тренировки = '))
raz2 = int(input('Введите минимальное значение диапозона = '))
raz3 = int(input('Введите максимальное значение диапозона = '))
print('====================сложение======================')
for i in range(1,raz+1):
    rand1=random.randint(raz2,raz3)
    rand2=random.randint(raz2,raz3)
    print(i,'.\t',rand1,'+',rand2,'=',end=" ")
    otvet = int(input())
    if otvet == rand1 + rand2:
        print('молодец')
        prav = prav + 1 #счетчик правильных ответов
    else:
        print('правильный ответ = ',rand1 + rand2)
        nprav = nprav + 1 #счетчик не правильных ответов
print('====================умножение======================')
for k in range(1,raz+1):
    rand1=random.randint(raz2,raz3)
    rand2=random.randint(raz2,raz3)
    print(k,'.\t',rand1,'*',rand2,'=',end=" ")
    otvet = int(input())
    if otvet == rand1 * rand2:
        print('молодец')
        prav = prav + 1 #счетчик правильных ответов
    else:
        print('правильный ответ = ',rand1 * rand2)
        nprav = nprav + 1 #счетчик не правильных ответов
print('Твой результат = ',prav)

