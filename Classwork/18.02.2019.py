import random
a = []
rand = random.randint(10,50000)
for i in range (rand):
       rand2 = random.randint(5,20)
       a.append(rand2)
#print(a)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for i in range (rand):
       for j in range (rand-1-i):
              print(a)
              if a[j] > a[j+1]:
                     #1
                     temp = a[j]
                     a[j] = a[j+1]
                     a[j+1] = temp
                     #2
                     #a[j], a[j+1] = a[j+1],a[j]
print(a)
