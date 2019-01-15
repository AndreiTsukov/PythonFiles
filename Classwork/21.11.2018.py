'''
s = int(input())
if s > 0:
    print('Абсолютное число',s,'= ',s)
else:
    print('Абсолютное значение отрицательного числа',s,'= ',-s)


s = int(input())
if s > 0:
    print('Абсолютное число',s,'= ',s)
if s <0:
    print('Абсолютное значение отрицательного числа',s,'= ',-s)
if s ==0:
    print('Число равно нулю')

x=int(input('Задайте ззначение x'))
y=int(input('задайте значение y' ))
if x > 0:
    if y > 0:
        print("I")
    else:
        print('IIII')
else:
    if y > 0:
        print("II")
    else:
        print('III')

a = int(input())
if a:
    print('10')

n = input('Enter your Name')
if n:
    print('Привет',n)
else:
    print('Enter for exit')
'''

#Задание 1
'''
a = int(input('введи а '))
 = int(input('введи x '))
if 1:
   print('STOP')
else:
    y = (a**2+3)/(x-1)
    print('Ваш ответ: ',y)
'''
#Zadanije 2

a= int(input('введи a '))
b= int(input('введи b '))
c= int(input('введи c '))
if a>b:
    if a>c:
        m=a
    else:
        m=c
else:
    if b>c:
        m=b
    else:
        m=c
print('Максимальное значение равно ',m)
'''
#Z3
x=int(input('Задайте ззначение x'))
y=int(input('задайте значение y' ))
if x > 0 and y< 0:
        print("I")
elif x > 0 and y < 0:
        print('IIII')
elif y > 0:
        print("II")
else:
    print('III')
'''
