class SultansDine:
    total_branch=0
    total_sell=0
    detailsdicc={}
    def __init__(self,name):
        self.branch=name
        self.sell=0
        SultansDine.detailsdicc[self.branch]=self.sell
        SultansDine.total_branch+=1

    def sellQuantity(self,quan):
        if self.branch=='Dhanmondi':
            self.sell+=quan*400
            SultansDine.detailsdicc[self.branch]+=self.sell
            SultansDine.total_sell+=self.sell
        elif self.branch=='Baily Road':
             self.sell+=quan*350   
             SultansDine.detailsdicc[self.branch]+=self.sell
             SultansDine.total_sell+=self.sell
        elif self.branch=='Gulshan':
             self.sell+=quan*300
             SultansDine.detailsdicc[self.branch]+=self.sell
             SultansDine.total_sell+=self.sell
    
    def branchInformation(self):
        print(f'Branch Name: {self.branch}\nBranch Sell: {self.sell} Taka')

    @classmethod
    def details(cls):
        print(f'Total Number of branch(s): {SultansDine.total_branch}')
        for i in SultansDine.detailsdicc.keys():
            print(f'Branch Name: {i}, Branch sell: {SultansDine.detailsdicc[i]}')
            temp=(100/SultansDine.total_sell)*SultansDine.detailsdicc[i]
            print(f"Branch consists of total sell's: {round(temp,2)}%")





SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
