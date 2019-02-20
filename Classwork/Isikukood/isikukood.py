#Проверка isikukood
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
              
