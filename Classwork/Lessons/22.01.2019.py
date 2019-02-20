#Алексе Крымский
#==========================================
#a = 'Информатика в 3 классе'
'''
a = input('>> ')
print(a, '\n')
k=len(a)
print('Индекс\tСимвол')
for i in range(k):
    if (a[i].isdigit()):
        print('В тексте цифра : ',a[i])
        print('Вышли из программы\n')
        break
    else:
        print(i,"\t",a[i])
print('Программа выполнена!')
input('НАжмите любую клавишу ...')
'''
name = input('What your name7 >> ')

print('HI,', name.capitalize())
