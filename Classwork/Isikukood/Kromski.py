#Проверка isikukood
#Уровень сложности : A
#Kromski
import datetime
'''
isikukood = ''
while not isikukood.isdigit() or int(isikukood[0]) != 3 and int(isikukood[0]) != 4 and int(isikukood[0]) != 5 and int(isikukood[0]) != 6 or int(len(isikukood)!=11):
       isikukood = input('Введите свой isikukood = ')
if int(isikukood[0]) == 3 or int(isikukood[0]) == 4:
       date = '19'
       if int(isikukood[0]) == 3:
              print('Пол = Мужской')
       elif int(isikukood[0]) == 4:
              print('Пол = Женский')
       d = isikukood[5:7]
       m = isikukood[3:5]
       y = date+isikukood[1:3]
       print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
       date = '20'
       if int(isikukood[0]) == 5:
              print('Пол = Мужской')
       elif int(isikukood[0]) == 6:
              print('Пол = Женский')       
       d = isikukood[5:7]
       m = isikukood[3:5]
       y = date+isikukood[1:3]
       print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
'''
              
#Уровень сложности : B
'''
now_date = datetime.date.today()
isikukood = ''
while not isikukood.isdigit() or int(isikukood[0]) != 3 and int(isikukood[0]) != 4 and int(isikukood[0]) != 5 and int(isikukood[0]) != 6 or int(len(isikukood)!=11):
       isikukood = input('Введите свой isikukood = ')
       #isikukood = str(50902275555)
       #isikukood = str(60902285555)
       #isikukood = str(39902265555)
if int(isikukood[0]) == 3 or int(isikukood[0]) == 4: #
       date = '19'
       if int(isikukood[0]) == 3:
              print('Пол = Мужской')
       elif int(isikukood[0]) == 4:
              print('Пол = Женский')
       d = isikukood[5:7]
       m = isikukood[3:5]
       y = date+isikukood[1:3]
       print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
       y = int(y)
       m = int(m)
       d = int(d)
       isikukood_date = datetime.date(y,m,d)
       year = now_date.year - isikukood_date.year
       if now_date.month <= isikukood_date.month:
              if now_date.day < isikukood_date.day:
                     year-=1
       print('Человеку = ',year,' лет')
elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
       date = '20'
       if int(isikukood[0]) == 5:
              print('Пол = Мужской')
       elif int(isikukood[0]) == 6:
              print('Пол = Женский')       
       d = isikukood[5:7]
       m = isikukood[3:5]
       y = date+isikukood[1:3]
       print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
       y = int(y)
       m = int(m)
       d = int(d)
       isikukood_date = datetime.date(y,m,d)
       year = now_date.year - isikukood_date.year
       if now_date.month <= isikukood_date.month:
              if now_date.day < isikukood_date.day:
                     year-=1
       print('Человеку = ',year,' лет')
'''
now_date = datetime.date.today()
isikukood = ''
m = True
def isikukods():                     
       if int(isikukood[0]) == 3 or int(isikukood[0]) == 4: #
              date = '19'
              if int(isikukood[0]) == 3:
                     print('Пол = Мужской')
              elif int(isikukood[0]) == 4:
                     print('Пол = Женский')
              d = isikukood[5:7]
              m = isikukood[3:5]
              y = date+isikukood[1:3]
              print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
              y = int(y)
              m = int(m)
              d = int(d)
              isikukood_date = datetime.date(y,m,d)
              year = now_date.year - isikukood_date.year
              if now_date.month <= isikukood_date.month:
                     if now_date.day < isikukood_date.day:
                            year-=1
              print('Человеку = ',year,' лет')
       elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
              date = '20'
              if int(isikukood[0]) == 5:
                     print('Пол = Мужской')
              elif int(isikukood[0]) == 6:
                     print('Пол = Женский')       
              d = isikukood[5:7]
              m = isikukood[3:5]
              y = date+isikukood[1:3]
              print('Дата = ',str(d)+'/'+str(m)+'/'+str(y))
              y = int(y)
              m = int(m)
              d = int(d)
              isikukood_date = datetime.date(y,m,d)
              year = now_date.year - isikukood_date.year
              if now_date.month <= isikukood_date.month:
                     if now_date.day < isikukood_date.day:
                            year-=1
              print('Человеку = ',year,' лет')
              
while not isikukood.isdigit() or int(isikukood[0]) != 3 and int(isikukood[0]) != 4 and int(isikukood[0]) != 5 and int(isikukood[0]) != 6 or int(len(isikukood)!=11):
       isikukood = input('Введите свой isikukood = ')
while m:
       m = 0
       otvet = 0
       j = 0 
       for i in range(1,10):
              otvet = int(isikukood[m]) * i
              m+=1
              j = j + otvet
              if i == 9:
                     otvet = int(isikukood[m]) * 1
                     j = j + otvet
       fff = str(j)[-1]
       zzz = str(isikukood[-1])
       if int(fff) + 1 == int(zzz) or int(fff) == int(zzz) :
              print('Ваш isikukood коректный')
              isikukods()
              break
       else:
              m = 0
              otvet = 0
              t = 0 
              for i in range(3,10):
                     otvet = int(isikukood[m]) * i
                     m+=1
                     t = t + otvet
                     if i == 9:
                            x = 0
                            otvet = int(isikukood[m]) * x
                            x+=1
                            t = t + otvet
                            #print(t)
              if int(t) == int(zzz) or int(t)+1 == int(zzz) :
                     print('Ваш isikukood коректный')
                     isikukods()
                     break
                     
              else:
                     print('Ваш isikukood не коректный')
                     break








       
