#kromski
'''
fin = open('test.txt','r')
fin_input = []
for line in fin.readlines():
       line = line.strip()
       fin_input.append(line)
fin.close()
print(fin_input)

fout = open ('output.txt','w')
#Создаем переменную в которой мы открываем файл в режиме w
#Eсли нету файла, то он создает новый
print("Hello, Hello",file = fout)
#Пишем запись "Hello" в файл
#После вызываться служебное слово file и имя переменной где открыт файл
fout.close()
#Мы должны обязаельно закрыть файл перед тем, как работать с ним в новом режиме
fin = open('output.txt','r')
#Создаем переменную в которой мы открываем файл в режиме r
a = fin.readlines()
#Передаем значение 
for line in a: #цикл удаляет спецсимволы
       line = line.strip()
       print(line)
fin.close()
'''
#variable 1
'''
fin = open('input.txt','r')
fin_input = []
for line in fin.readlines():
       line = line.strip()
       fin_input.append(line)
       print(line)
fin.close()
                        
                        
fout = open ('newfile.txt','w')
for line in fin_input:
       print(line,file = fout)
fout.close()

#variable 2
inp = open('input.txt','r')
out = open('output.txt','w')
inp_input = []
for line in inp.readlines():
       line = line.strip()
       inp_input.append(line)    
for line in inp_input:
      print(line,file = out)
inp.close()
out.close()

fin = open('input.txt','r')
print(fin.read())

'''

