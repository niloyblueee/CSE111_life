class Farmer:
    def __init__(self,name='',id=0):
        if name=='':
            print("Welcome to your farm!")
        elif id==0:
            self.name=name
            print(f'Welcome to your farm, {self.name}!')
        else:
            self.id=id
            print(f'Welcome to your farm, {self.id}!')        
        self.crops=[]
        self.fishes=[]
    def addCrops(self,*crops):
        if len(crops)!=0:
            print(f'{len(crops)} crop(s) added')
        else:
            print("No Fish added")
        for i in crops:
            self.crops.append(i)
    def addFishes(self,*fishes):
        if len(fishes)!=0:
            print(f'{len(fishes)} crop(s) added')
        else:
            print("No Fish added")            
        for i in fishes:
            self.fishes.append(i)
    def showGoods(self):
        if len(self.crops)==0:
            print("You don't have any crop(s).")
        else:
            print(f'You have {len(self.crops)} crop(s):')
            print(", ".join(self.crops))
        if len(self.fishes)==0:
            print("You don't have any fish(s).")
        else:
            print(f'You have {len(self.fishes)} fish(s):')
            print(", ".join(self.fishes))

f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")
