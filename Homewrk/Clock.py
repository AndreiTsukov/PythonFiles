s = 0
for i in range(0,3):
    for k in range(0,4):
        for e in range(0,6):
            for r in range (0,10):
                print(i,k,':',e,r)
                if i == r and k == e:
                    print('+')
                    s+=1
print(s)
