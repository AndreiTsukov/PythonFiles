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
#Уровень сложности C
now_date = datetime.date.today()
isikukood = ''
proverka = True
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
              if isikukood_date == now_date:
                     print('С днем рождения!')
              
while not isikukood.isdigit() or int(isikukood[0]) != 3 and int(isikukood[0]) != 4 and int(isikukood[0]) != 5 and int(isikukood[0]) != 6 or int(len(isikukood)!=11):
       isikukood = input('Введите свой isikukood = ')
while proverka:
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
                j = str(j)
       if int(j[-1])+1 != int(isikukood[-1]):
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
              j = str(j)
              if int(j[-1])+1 != int(isikukood[-1]):
                     print('Ваш исикукод не действительный')
                     break
              elif int(j[-1])+1 == int(isikukood[-1]):
                     print('Ваш исикукод действительный')
                     isikukods()
                     break
       elif int(j[-1])+1 == int(isikukood[-1]):
                     print('Ваш исикукод действительный')
                     isikukods()
                     break
              








       
