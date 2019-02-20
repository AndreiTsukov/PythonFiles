'''
i = 1
for color in 'red','orange','yellow','green','cyan','blue','violet':
    print('#',i,' color of rainbow is ',color)
    i += 1
+@+@+@++@+@+@+@@+@++@+@+@+@+@+@+@@+@+@+@+@++@+@+@+@+@++@+@+@@++@+@@

for i in range(10):
    print(i,'\t' , i ** 2 )
print('End')

sum = 0
n = 10
print('число','\t','сумма')
for  i in range(1, n + 1 ):
    sum += i
    print(i,'\t',sum)
print('итог = ',sum)


print('четные числа от 2 до 100')
for i in range(2,101,2):
    print(i)

print('нечетные числа от 1 до 100')
for i in range(1,101,2):
    print(i)

print('десятки в убывающем порядке')
for i in range(100,9,-10):
    print(i)

a = 1
b = 2
c = 3
print(a,b,c)
print(a,b,c, sep = '|', end = ',! ')
print(a,b,c, sep = '|', end = '!!!!')

import random
summa = 0
n = int(input('Enter your number ==> '))
for i in range(1,n+1):
    if i == n:
        print(rand, end =',')
    rand = random.randint(1,100)
    summa = summa + rand
    print(rand, end =',')
    if i < n:
        print(rand, end =',')
    else:
        print(rand)
print('сумма всех рандомных чисел == ',summa)

import random
ot = 0
for i in range(1,6):    
    rand = random.randint(1,20)
    rand2 = random.randint(1,20)
    print(i,'.\t',rand,'+',rand2,'=',end=' ')
    a = int(input(''))
    if a == rand + rand2:
        ot = ot + 1
print('количество правельных ответов =',ot)
 '''
s='asfdsfsdf'
print(s[1:])
