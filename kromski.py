import random
summa = random.randint(1,1000)
i=0
popitki=0
while i==0: 
    pin =int(input('Введите свой пин код: '))
    if pin == 1234:
        print('Вы вошли успешно')
        k=1
        break
    elif pin !='1234':
        popitki+=1
        print('Неверный пинкод. Ваши попытки = ',popitki)
        if popitki == 3:
            print('Ваши попытки закончились!')
            k=0
            break
while k==1:
    print(' 1 - Посмотреть счет ')
    print(' 2 - Снять деньги ')
    print(' 3 - Пополнить счет ')
    print(' 4 - Выйти ')
    bank_command=int(input('Введите цыфру команды: '))
    if bank_command == 1:
        print('Состояние вашего счета= ',summa)
        input('Нажмите Enter')
    elif bank_command == 2:
        if summa < 0:
            print('Состояние вашего счета= ',summa)
            print('Не хвотает денег на счету')
            input('Нажмите Enter')
        elif summa > 0 :
            print('Состояние вашего счета= ',summa)
            while i==0:
                bank_snjatie=int(input('Сколько денег вы хотите снять = '))
                if bank_snjatie <= 0:
                    print('Вы ввели отрицательное число или 0 ')
                else:
                    if summa <= 0:
                        print('Ваш счет в равен 0 или в отрицательном значении')
                    else:
                        summa = summa - bank_snjatie
                        print('Деньги сняты успешно ')
                        print('Состояние вашего счета= ',summa)
                        input('Нажмите Enter')
                        break
    elif bank_command == 3:
            print('Состояние вашего счета= ',summa)
            while i==0:
                bank_vznos=int(input('Сколько денег вы хотите внести = '))
                if bank_vznos <= 0:
                    print('Вы ввели отрицательное число или 0 ')
                else:
                    summa = summa + bank_vznos
                    print('Деньги внесены успешно ')
                    print('Состояние вашего счета= ',summa)
                    input('Нажмите Enter')
                    break
    elif bank_command == 4:
        while i == 0:
            bank_exit = int(input('Вы точно хотите выйти? 1-Да 2-Нет '))
            if bank_exit ==1:
                k=0
                break
            elif bank_exit ==2:
                print('Вы вернулись в систему')
                break
            else:
                print('Вы  ввели неподходящее значение')
        
print('До Свидания! ')       
        
              


 
