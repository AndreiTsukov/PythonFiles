import random
f = True
prav = 0
raz = 0
rad1 = 0
rad2 = 0
print('*******************************************************************')
print('Тема : Применение цыклов')
print('Автор работы: Алексей Крымский')
print('Уровень сложности работы C')
print('*******************************************************************')
print('!!!Данный тест проверит ваши знания и скорость!!!\n В этой программе предоставлены возможности: ')
print(' - Изменение параметров интервала чисел \n - Изменения кол.-во заданий \n По стандарту стоит: ')
print(' - 5 вопросов \n - интервал от 1 до 50 \n !!!Приятного прохождения теста!!!')
print('*******************************************************************')
print('1 - свои настройки')
print('2 - стандартные настройки настройки')
begin = int(input('Выбор настроек = '))
if begin == 1:
    raz = int(input('количество заданий = '))
    rad1 = int(input('минимальный интервал генерации случайных чисел = '))
    rad2 = int(input('максемальный интервал генерации случайных чисел = '))
elif begin == 2:
    raz = 5
    rad1 = 1
    rad2 = 50
else:
    print('invalid command')
while f:
    for r in range(1,raz+1):
        rand1 = random.randint(rad1,rad2)
        rand2 = random.randint(rad1,rad2)
        print(r,'.\t',rand1,'+',rand2,' = ', end =' ')
        otvet = int(input())
        if otvet == rand1 + rand2:
            print('молодец')
            prav+=1
        else:
            print('Ответ должен быть = ',rand1 + rand2)
    protsent = (prav * 100 )/raz
    print('Твой результат : ', prav,' из ',raz,', это ',protsent,'%')
    povtor  = input('Хотите повторить тест y/n = ')
    if povtor == 'n':
        break
    elif povtor == 'y':
        prav = 0
    
        
    
