import random
prav = 0
nprav = 0
raz = int(input('Количество заданий для тренировки = ')
a = int(input('Введите радиус1 = ')
b = int(input('Введите радиус2 = ')
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
print('Твой результат = ',prav,)

