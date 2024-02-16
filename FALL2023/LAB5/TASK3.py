class Spaceship:
    def __init__(self,name,cap):
        self.name=name
        self.capacity=cap
        self.tempcapa=cap
        self.cargo=[]
        self.carryweight=0
    def load_cargo(self,cargo):
        if not cargo.getweight() > self.capacity:
            self.cargo.append(cargo.getname())
            self.tempcapa-=cargo.getweight()
            self.carryweight+=cargo.getweight()
        else:
            print(f'Warning: Unable to load Neutronium inside Falcon. Exceeds capacity by {abs(self.tempcapa-cargo.getweight())}.')   
    def display_details (self): 
        print(f'Spaceship Name: {self.name}\nCapacity: {self.capacity}\nCurrent Cargo Weight: {self.carryweight}\nCargo: {self.cargo}')  
class Cargo: #private
    def __init__(self,name,weight):
        self.__name=name
        self.__weight=weight
    def getweight(self):
        return self.__weight
    def getname(self): 
        return self.__name   
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









