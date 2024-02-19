#3.1
class Contacts:
  def __init__(self,nameL,numberL):
    self.name=nameL
    self.numbers=numberL
    self.contactDict={}
    if len(self.name)!=len(self.numbers):
      print("Contacts cannot be saved. Length Mismatch!")
    else:
      for i in self.name:
        for j in self.numbers:
          self.contactDict[i]=j
      print(f'Contacts saved successfully.')

names = ["Emergency", "Father", "Bestie"]
numbers = ["999", "01xx23", "01xx87", "01xx65", "01xx43"]
m1 = Contacts(names, numbers)
m3=m1
print("Saved Contacts:", m1.contactDict)
print("---------------------------------------------")
names.append("Mother")
numbers.pop()
m2 = Contacts(names, numbers)
print("Saved Contacts:", m2.contactDict)

#3.2
m1 = Contacts(names, numbers)
print('OLD ADDRESS',m3,'NEW ADDRESS',m1,sep='\n')
print(f'new: {m1.contactDict}')