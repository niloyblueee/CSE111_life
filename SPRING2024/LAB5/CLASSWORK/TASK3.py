class TaxiLagbe:
    def __init__(self,num,area):
        self.numplate=num
        self.area=area
        self.capacity=4
        self.passenger=[]
        self.taka=0
    def addPassenger(self,*passen):
        for i in passen:
            if self.capacity!=0:
                self.passenger.append(i.split('_')[0])
                self.capacity-=1   
                self.taka+=int(i.split('_')[1])
                print(f'Dear {i.split('_')[0]}! Welcome to TaxiLagbe.')
            else:
                print("Taxi Full! No more passengers can be added.")    
    def printDetails(self):
        print(f'Trip info for Taxi number: {self.numplate}\nThis taxi can only cover the {self.area} area.')
        print(f'Total passengers: {len(self.passenger)}\nPassenger lists:{', '.join(self.passenger)}')
        print(f'Total collected fare: {self.taka} Taka')

taxi1 = TaxiLagbe('1010-01', 'Dhaka')
print('-------------------------------')
taxi1.addPassenger('Walker_100', 'Wood_200','Matt_100')
taxi1.addPassenger('Wilson_105')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi1.addPassenger('Karen_200')
print('-------------------------------')
taxi1.printDetails()
print('-------------------------------')
taxi2 = TaxiLagbe('1010-02', 'Khulna')
taxi2.addPassenger('Ronald_115', 'Parker_215')
print('-------------------------------')
taxi2.printDetails()

