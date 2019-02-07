u = ''
while not u.isdigit() or int(u)<=1:
       u = input('Введите натуральное число>> ')
u = int(u)
print(u,end =' ')
while u !=1:
       if u % 2 == 0:#четные
              u = u / 2
              summ = u
       elif u % 2 != 0:
              u = u * 3
              u += 1 
              u = u / 2
              summ = u
       print(int(summ),end = ' ')
              
