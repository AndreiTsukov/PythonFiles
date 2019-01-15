'''
row = int(input())
col = int(input())
for i in range(row):
    #print('i = ',i)
    for y in range(col):
        print('*', end = ' ')
    print()

row = int(input())
col = int(input())
for i in range(row):
    for j in range(row):
        if i == j:
            break
        print('*', end = ' ')
    print()


row = int(input())
col = int(input())
for i in range(row):
    row = i + 1
    for j in range(row):
        print('*', end = ' ')
    print()

row = int(input())
col = int(input())
for i in range(row):
    for j in range(i):
        print('*', end = ' ')
    print()

row = int(input())
col = int(input())
for i in range(row):
    row = row - 1
    for j in range(row):
        print('*', end = ' ')
    print()

row = int(input())
col = int(input())
for i in range(row):
    row = row - 1
    for j in range(row + 1):
        print('*', end = ' ')
    print()

row = int(input())
for i in range(row):
    row = i + 1
    for j in range(1,row+1):
        print(j, end = ' ')
    print()

row = int(input())
for i in range(row):
    row = i + 1
    for j in range(row):
        print('*', end = ' ')
    print()

row = int(input())
for i in range(row):
    row = i + 1
    for j in range(1,row+1):
        print(j, end = ' ')
    print()

suvin = 0
for i in range(0,10):
    for k in range(0,10):
        for j in range(0,10):
            for b in range(0,10):
                for a in range(0,10):
                    if i == 4 or k == 4 or j == 4 or b == 4 or a ==4:
                        suvin+=1
                    elif i == 1 and k == 3 or k == 1 and j == 3 or j == 1 and b == 3 or b == 1 and a == 3 :
                        suvin+=1
                   
                    
print('Всего придеться убрать техники = ',suvin)
'''
suvin = 0
for i in range(0,24):
    for k in range(0,60):
        #print(i,k)
        z = str(i,k)
        if z == i and k or k and i:
            suvin+=1
                   
print(i,k)                    
print('Симетричные появляються = ',suvin)

























                        
    
