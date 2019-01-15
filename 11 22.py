#Z1
'''
a=int(input('Введи первое число '))
b=int(input('Введи второе число '))
if a>b:
    r=a-b
elif a<b:
    r=a+b
else:
    r=a
print(r)
'''
#Z2
"""
m=int(input('Введите число '))
if m == 1:
    print('Январь')
elif m == 2:
    print('Февраль')
elif m == 3:
    print('Март')
elif m == 4:
    print('Апрель')
elif m == 5:
    print('Май')
elif m == 6:
    print('Июнь')
elif m == 7:
    print('Июль')
elif m == 8:
    print('Август')
elif m == 9:
    print('Сентябрь')
elif m == 10:
    print('Октябрь')
elif m == 11:
    print('Ноябрь')
elif m == 12:
    print('Декабрь')
else:
    print('Некоректнное число')
"""
#3 число крастно 2ум и кратно 3ем
'''
n = int(input('Введи число: '))
if n%2==0 and n%3==0:
    print('Число кратное')
else:
    print('Число не кратное')
'''
#4
'''
n = int(input('Введи число: '))
if n%2==1 or n%5==0 :
    print('Число нечетное и кратное 5 ')
else:
    print('Число не соответствует критерию')
'''
#Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна
#вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа
#различны)
'''
a=int(input('Vvedi pervoe 4islo'))
b=int(input('Vvedi vtoroe 4islo'))
c=int(input('Vvedi tretje 4islo'))
#if a==b==c:
if a==b and b==c and c==a:
    print('3')
elif a==b or b==c or c==a:
    print('2')
else:
    print('0')
'''

































