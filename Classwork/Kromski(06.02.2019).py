f1 = f2 = 1
n = ''
while not n.isdigit() or int(n)<1 or int(n)> 15: #1
       n = input('Укажите номер элемента послежовательности от 1 до 15: ')
       #Первый цыкл нужен для проверки того, что ввел человек.
       #Нужно, чтобы вводимое значение не являлось буквой или
       #Цифрой меньше 0 и цифрой не больше 15
       print('+')
n = int(n)
if n == 1:
       print(f1)
elif n == 2:
       print(f2)
else:
       print(f1,f2,end = ' ')
       i = 0
       while i < n - 2: #2
              f_sum = f1 + f2
              f1 = f2
              f2 = f_sum
              i += 1
              print(f2,end =' ')
       #Второй цыкл нужен для подсчета и вывода двух переменных(f1,f2)
       #Цыкл будет продолжаться до того момента пока i будет равно n-2(количество раз - два)
       #1.Он создает переменную f_sum в которой складываються две переменные(f1,f2)
       #2.Цыкл присваеват значение f2 переменной f1
       #3.Цыкл присваевает значение f_sum переменной f2
       #4.Увеличиваеться значение i для цыкла
       #5.Выводиться в строчку значения f2, которое имеет значение переменной f_sum(f1+f2)
       #Цыкл будет выполняться до тех пор, пока i не будет больше чем n-2(количество раз - два)
              
              
