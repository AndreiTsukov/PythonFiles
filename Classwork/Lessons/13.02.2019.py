'''
a = input('Задайте числовю последовательность > ').split()
print(a)
for i in range(len(a)):
       a[i] = int(a[i])
print(a)

a = [int(s) for s in input().split()]
print(a)

import random
i = 0
a = []
while i != 10:
       a.append(random.randint(5,20))
       i+=1
#print(' '.join([str(i) for i in a]))
#2
for m in range(len(a)):
       a[m] = str (a[m])
s = (' '.join(a))
print(s)

#1
print(a)
i = 0
s = str('')
for m in a:
       a[i] = str(m)
       i+=1
s =(' '.join(a))
print(s)

a = [0] * int(input('Количество жлементов в списке > '))
print(a)
for i in range(len(a)):
       print(str(i+1)+'. ',end =' ')
       a[i]= int(input('Укажите значение элемента списка > '))
print(a)
for i in range(len(a)):
       print(a[i],end=' ')

#PRAKTIKUM
import random
i = 10
a = []
while i != 20:
       a.append(random.randint(1,20))
       i+=1
print(a)
m = 0
for i in range(1,len(a)-1):
       if a[i] > a[i-1] and a[i] > a[i+1]:
              m+=1
              print(str(m) + '.', a[i-1],a[i],a[i+1])
       

import random
import datetime
i = 10
a = []
print('Дата: ',datetime.date.today())
while i != 20:
       a.append(random.randint(1,20))
       i+=1
print(a)
m = a[0]
k = 0
z = a[0]
x = 0
for i in range(1,len(a)-1):
       if a[i] > m:
              m = a[i]
for i in range(len(a)):
       if m == a[i]:
              print('[' + str(i) + ']',m)
'''
import datetime
now_date = datetime.date.today()
now_time = datetime.date.today()
cur_year = now_date.year
cur_month = now_date.month
cur_day = now_date.day
print(cur_year)
print(cur_month)
       
print(cur_day)
              
              
       
       

              
       
              
























