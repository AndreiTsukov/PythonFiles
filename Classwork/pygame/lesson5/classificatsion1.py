'''
class cat():
       name = ""
       color = ""
       weight = 0
       def meow(self):
              print('meow,',self.name)
animal = cat()
animal2 = cat()
animal.name = "Клубок"
animal.color = "Красный"
animal.weight = 3
animal2.name = "Зеленка"
animal2.color = "Красный"
animal2.weight = 4
animal2.meow()
animal.meow()
'''

class address():
       name=''
       line1=''
       line2=''
       city=''
       state=''
       zip=''
       def printAddress(self):
              print(self.name)
              if(len(self.line1) > 0):
                     print(self.line1)
              if(len(self.line2) > 0):
                     print(self.line2)
              print(self.city+", "+self.state+" "+self.zip)
adr = address()
adr.name = "John"
adr.line1 = "1222 Str. Smit"
adr.line2 = ""
adr.city = "Panama city"
adr.state = "FL"
adr.zip = "20133"
adr.printAddress()







