class Spaceship: #public
  def __init__(self,name,cap):
    self.name,self.cap=name,cap
    self.cargo,self.carry=[],0

  def load_cargo(self,other):
    if int(other.getAttributes()[1])+self.carry<self.cap:
      self.cargo.append(other.getAttributes()[0])
      self.carry+=int(other.getAttributes()[1])
    else:
      print(f'Warning: Unable to load {other.getAttributes()[0]} inside {self.name}. Exceeds capacity by {int(other.getAttributes()[1])-(self.cap-self.carry)}')
  def display_details(self):
    print(f'Spaceship Name: {self.name}\nCapacity: {self.cap}\nCurrent Cargo Weight: {self.carry}\nCargo: {self.cargo}')
class Cargo: #private
  def __init__(self,name,weight):
    self.__name,self.__weight=name,weight
  def getAttributes(self):
    return self.__name , self.__weight
  def setName(self,name):
    self.__name=name
  def setWeight(self,Weight):
    self.__weight=Weight
# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()
