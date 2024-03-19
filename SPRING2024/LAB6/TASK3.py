class Vaccine:
  def __init__(self,name,org,delay):
    self.name,self.org,self.delay=name,org,delay

class Person:
  def __init__(self,name,age,job="General Citizen"):
    self.name,self.age,self.job=name,age,job
    self.vacc=''
    self.dose1=False
    self.dose2=False
  def pushVaccine(self,vacc,dose="1st Dose"):
      if self.vacc=='' and dose=="1st Dose":
        self.vacc=vacc.name
        self.dose1=True
        self.delay=vacc.delay
        print(f'1st dose done for {self.name}')
      elif dose=="2nd Dose" and self.vacc!=vacc.name:
        print(f'Sorry {self.name}, you can’t take 2 different vaccines')
      elif dose=="2nd Dose" and self.vacc==vacc.name:
        self.dose2=True
        print(f'2nd dose done for {self.name}')

  def showDetail(self):
    if self.dose1==True  and self.dose2==False:
      print(f'Name: {self.name} Age: {self.age} Type: {self.job}\nVaccine name: {self.vacc}')
      print(f'1st dose: Given\n2nd dose: Please come after {self.delay} days')
    elif  self.dose1==True  and self.dose2==True:
      print(f'Name: {self.name} Age: {self.age} Type: {self.job}\nVaccine name: {self.vacc}')
      print(f'1st dose: Given\n2nd dose: Given')


astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")
