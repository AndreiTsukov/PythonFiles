#Kontrol töö
'''
a = int(input('Введите значение 1: '))
b = int(input('Введите значение 2: '))
while a != b:
    if a < b:
        x = a
        a = b
        b = x
    a = a - b                
h=a
print(h)
'''
#+++++++++++++++++++++++++++++++++++++++
import math
start = int(input('Введите значение a: '))
a1= start // 100
a2= (start // 10) % 10 
a3= start % 10

if a1 > a2:  
    if a1 > a3:
        a = a1
    else:
        a = a3
else:
    if a2 > a3:
        a = a2
    else:
        a = a3
if a1 < a2:  
    if a1 < a3:
        h = a1
    else:
        h = a3
else:
    if a2 < a3:
        h = a2
    else:
        h = a3
print('Самое большое число: ',a)
print('Самое маленькое число: ',h)
if a % 2 == 0 :
    z = math.sqrt(start)
    print('Квадратный корень',z)
if  h%3==0:
    z1 = math.exp(start)
    print('Кубический корень - ',z1)
    



    
