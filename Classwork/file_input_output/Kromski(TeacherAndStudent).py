import random
tehete_arv = int(input("Sisestage tehete arv: "))
f1 = open("student.txt", "a")
print('Выполните задания = ',tehete_arv, file = f1)
f2 = open("teacher.txt", "a")
print('Ответы на ',tehete_arv,' заданий', file = f2)
f2.close()
for i in range(tehete_arv):   
       a = random.randint(0,10)
       b = random.randint(0,10)
       tehe = random.randint(1,4)
       oige_vastus = 0
       if tehe == 1: #liitmine
              oige_vastus = a + b
              avaldis = str(a) + " + " + str(b) + " = "
       elif tehe == 2: #lahutamine
              while a < b:
                     a = random.randint(0,10)
              oige_vastus = a - b
              avaldis = str(a) + " - " + str(b) + " = "
       elif tehe == 3: #korrutamine
              oige_vastus = a * b
              avaldis = str(a) + " * " + str(b) + " = "
       elif tehe == 4: #jagamine
              while b == 0:
                     b = random.randint(0,10)       
              oige_vastus = round(a / b, 2) #ümardame 2 komakohani
              avaldis = str(a) + " / " + str(b) + " = "       
       f1 = open("student.txt", "a")
       f1.write(avaldis + "\n")
       f1.close()
       f2 = open("teacher.txt", "a")
       f2.write(avaldis + str(oige_vastus) + "\n")
       f2.close()
f1 = open("teacher.txt", "a")
print('==============================================', file = f1)
f1.close()
f1 = open("student.txt", "a")
print('==============================================', file = f1)
f1.close()
