class Farmer:
    def __init__(self,any=''):
            if any=='':
                print(f'Welcome to your farm!')
            elif type(any)==int:
                print(f'Welcome to your farm! Your farm id is {any}')
            else:
                print(f'Welcome to your farm, {any}')
            self.crops=[]
            self.fishes=[]
            self.crcount=0
            self.fshcount=0
    def addCrops(self,*crops):
        count=0
        for crop in crops:
            self.crops.append(crop)
            count+=1    
        if count!=0:
            print(f'{count} crop(s) added.')
        else:
             print('No crop(s) added.')
        self.crcount+=count
        count=0
    def addFishes(self,*fishes):
        count=0
        for fish in fishes:
            self.fishes.append(fish)
            count+=1
        if count!=0:
            print(f'{count} fish(s) added.')    
        else:
             print('No fish(s) added.')
        self.fshcount+=count
        count=0

    def showGoods(self):
        if self.crcount!=0:
            crops=','.join (self.crops)
            print(f'You have {self.crcount} crops(s) :\n{crops}')
        else:
             print('You dont have any crop(s)') 
        if self.fshcount!=0:
            fish=','.join (self.fishes)
            print(f'You have {self.fshcount} fishes(s) :\n{fish}')  
        else:
            print('You dont have any fish(s)')    

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