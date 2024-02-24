class GreenPhone:
    def __init__(self,mod,andrd,cam):
        self.model=mod
        self.android=andrd
        self.camera=cam
        if 'A' in mod:
            self.coverage=2
        elif 'M' in mod:
            self.coverage=3
        else:
            self.coverage=4    
    def showSpecification(self):    
        print(f'Phone Company: GreenPhone\nModel Name: {self.model}\nAndroid Version: {self.android}\nNumber of Cameras: {self.camera}')
    def updatePhone(self):
        if self.coverage!=0:
            self.android+=1
            print(f'Your phone Greenphone {self.model} is upgraded to Android Version: {self.android}.')
            self.coverage-=1
        else:
            print(f'Your phone Greenphone {self.model} is already up to date.')    

print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()