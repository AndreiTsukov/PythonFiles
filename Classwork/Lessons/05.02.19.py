# for
# while
#Получить каждый символ и его индекс
'''
a = 'Programmerimine'
index = 0
for symbol in a :
    print(symbol, index)
    index+=1

a = 'Programmerimine'
for i in range ( len ( a ) ) :
    print(a[i],i)

a = 'Programmerimine'
i=0
while i  < len(a):
    print(a[i],i)
    i+=1

valik = ''
while not valik in ('1','2','3','4','5'):
    valik = input('ваш выбор ')

import random
a = []
n = int(input('Количество раз = '))

for i in range(n):
    rand = random.randint(1,100)
   # new_elem = rand
    a.append(rand)
    if i < a[i]:
        m = a[i]
print(a)
m = 0
for i in range(n ):
    if a[i] > m:
        m = a[i]
print(m)

import random
a = [0]*int(input())
print(a)
for i in range(len(a)):
    rand = random.randint(1,100)
    a[i]= rand
print(a)

s = 'a3254325c 43fr32562f54g657g55ad25s32fdbg34f3245bgf'
d = []
for symbol in s :
    if  '1234567890'.find(symbol) != -1:
        d.append(int(symbol))
print(d)

d = []
a = 'Pro12gr213am32mer453imi54ne'
for i in a:
    if i.isdigit():
        d.append(int(i))
print(d)
   '''     
import random
rand = random.randint(5,10)
a = []
for i in range(rand):
    rand = random.randint(1,10)
    a.append(rand)
print(a)
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        print(a[i],a[i+1])
