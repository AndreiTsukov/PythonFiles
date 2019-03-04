#контрольная сумма с помощью варианта 1
'''
isikukood = '50208302215'
otvet = 0
t = 0
m = 0
j = 0
for i in range(1,10):
     otvet = int(isikukood[m]) * i
     m+=1
     j = j + otvet
     if i == 9:
         otvet = int(isikukood[-2]) * 1
         j = j + otvet
print('-',j)
'''
#контроьная сумма с вариантом 2
isikukood = '50208302215'
otvet = 0
t = 0
m = 0
j = 0
for i in range(3,10):
     otvet = int(isikukood[m]) * i
     m+=1
     j = j + otvet
     if i == 9:
         for z in range(1,4):
             otvet = int(isikukood[m]) * z
             m+=1
             j = j + otvet
print('-',j)
