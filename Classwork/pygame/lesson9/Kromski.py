class Table:
    def __init__(self,l,w,h): #атрибут
        self.lenght = 1 #длинна
        self.width = w
        self.height = h

class KitchenTable(Table):
    def setPlaces(self,p):
        self.places = p

class DeskTable(Table):
    def squsare(self):
        return self.width * self.height

'''
если мы создадим объект на основе KitchenTable() и не укажим аргумениты то будет ошибка (__init__)
'''

t1 = KitchenTable(2,2,0.7) # аргумент
t2 = DeskTable(1.5,0.8,0.75)
t3 = KitchenTable(1,1.2,0.8)

tt = Table(1.5,0.6,0.8)
print('ploshad = ',t2.squsare())
