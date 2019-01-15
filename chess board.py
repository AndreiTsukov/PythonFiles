'''
#Вариант1
#Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а
#если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 каждое,
#задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

col1=int(input('Задайте значение числа: '))
row1=int(input('Задайте значение числа: '))
col2=int(input('Задайте значение числа: '))
row2=int(input('Задайте значение числа: '))

if ((col1+row1) % 2==0 and(col2+row2) % 2 == 0) :#четные 
    print('Yes')
if ((col1+row1) % 2==1 and(col2+row2) % 2 == 1):#нечетные
    print('Yes')
else:
    print('No')

#Вариант2
col1=int(input('Задайте значение числа: '))
row1=int(input('Задайте значение числа: '))
col2=int(input('Задайте значение числа: '))
row2=int(input('Задайте значение числа: '))
if (col1+row1) % 2==0 and(col2+row2) % 2 == 0\
   or (col1+row1) % 2 == 1 and(col2+row2) % 2 == 1:
        print('Yes')
else:
    print('No')

#Вариант3
col1=int(input('Задайте значение числа: '))
row1=int(input('Задайте значение числа: '))
col2=int(input('Задайте значение числа: '))
row2=int(input('Задайте значение числа: '))
if ((col1+row1) % 2==0 and(col2+row2) % 2 == 0) :#четные 
    print('Yes black')
elif ((col1+row1) % 2==1 and(col2+row2) % 2 == 1):#нечетные
    print('Yes white')
else:
    print('No')

#Вариант4
col1=int(input('Задайте значение числа: '))
row1=int(input('Задайте значение числа: '))
col2=int(input('Задайте значение числа: '))
row2=int(input('Задайте значение числа: '))
if (col1+row1) % 2 == 0 == (col2+row2) % 2:
    print('Yes ')
else:
    print('No')
    '''
#Вариант5
col1=int(input('Задайте значение числа: '))
row1=int(input('Задайте значение числа: '))
col2=int(input('Задайте значение числа: '))
row2=int(input('Задайте значение числа: '))
if (col1+row1+col2+row2) % 2 == 0:
    print('Yes ')
else:
    print('No')

