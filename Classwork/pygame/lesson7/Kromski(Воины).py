'''
class Person:
       def setName(self,n,s):
              self.name = n
              self.surname = s
p1 = Person()
p1.setName('Aleksei','Kromski')
print(p1.name,p1.surname)

class Person2:
       def __init__(self,n,s):
              self.name = n
              self.surname = s
p2 = Person2('Sam','Baker')
print(p2.name,p2.surname)

class Rectangle:
       def __init__(self,w = 0.5, h = 1):
              self.width = w
              self.height = h
       def square(self):
              return self.width * self.height

rec1 = Rectangle(5,2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h = 4)
print("Площади прямоугольника")
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())

class Employee:
       'Общий базовый класс'
       empCount = 0
       def __init__(self, name, salary):
              self.name = name
              self.salary = salary
              Employee.empCount += 1
       def displayCount(self):
              print('Всего сотрудников', Employee.empCount)
       def displayEmployee(self):
              print('Имя :', self.name, 'Зарплата: ', self.salary)
print(Employee)
print(Employee.__doc__)
emp1 = Employee('Andery',8000)
emp2 = Employee('Alex',7000)
emp2 = Employee('Sanja',9000)
emp1.age = 37
emp2.age = 87
emp1.displayEmployee()
emp2.displayEmployee()
print('Всего сотрудников',Employee.empCount)
print('Имя: ', emp1.name, ', Возраст: ',emp1.age)
print('Имя: ', emp1.name, ', Зарплата: ',emp1.salary)
'''
import random
class Voin():
       'Базовый класс воина'
       health = 100
       def __init__(self, name):
              self.name = name


              
def kick(firstkick):
       if firstkick == 1:
              voin2.health -= 20
              print('Удар ',voin1.name,' Осталось у другого воина = ',voin2.health,'\n')

       else:
             voin1.health -= 20
             print('Удар ',voin2.name,' Осталось у другого воина= ',voin1.health,'\n')
       
voin1 = Voin('Charseter')
voin2 = Voin('Vegaliser')
while voin1.health > 0 and voin2.health > 0:
       firstkick = random.randint(0,1)
       kick(firstkick)
if voin1.health > voin2.health:
       print('Победил',voin1.name,' здоровья = ', voin1.health)
else:
       print('Победил',voin2.name,' здоровья = ', voin2.health)
       

      
              
              
              
              



       
       
