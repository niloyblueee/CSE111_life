class TaxiLagbe:
    def __init__(self,s1,s2):
        s11=int(s1[:4])
        s12=int(s1[5:])
        self.cover=s2
        self.numplate=s1
        self.seats=4
        self.fare=0
        self.passname=[]
        self.passcount=0
    def addPassenger(self,*names):
        fare=0
        passname=''
        passcount=0
        if self.seats!=0:
            for name in names:
                fare=0
                passname=''
                for i in range(len(name)):
                    if name[i] == '_':
                        n=i
                        fare=int(name[n+1::])
                        passname=name[:i]
                        break
                self.passname.append(passname)
                self.passcount+=1
                passcount+=1
                self.seats-=1
                self.fare+=fare
            for i in range(passcount):
                print(f'Dear {self.passname[i]}! Welcome to Taxilagbe')
        else:
            print(f'Taxi Full! No more passengers can be added.')        
    def printDetails(self):
        passname=', '.join(self.passname)
        s11=int(self.numplate[:4])
        s12=int(self.numplate[5:])
        print(f'Trip info for Taxi number: {s11}-{s12}\nThis taxi can only cover the {self.cover} area.\nTotal passemger: {self.passcount}')
        print(f'Passenger list: \n{passname}\nTotal collected fare: {self.fare}')            



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
