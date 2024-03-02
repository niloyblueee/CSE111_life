class CellPackage:
    def __init__(self,price,data,talk_time,messages,cashback,validity):
        self.data=int(data[:len(data)-3:])*1024
        if self.data!=0:
            print(f'Data ={self.data} MB')
        self.talk_time=talk_time
        if self.talk_time!=0:
            print(f'talktime = {self.talk_time} Minutes')
        self.messages=messages
        if self.messages!=0:
            print('SMS/MMS =',self.messages)
        self.cashback=int(cashback[:len(cashback)-1:1])
        self.validity=validity
        if self.validity!=0:
            print(f'validity = {self.validity} Days')
        self.price=price
        if self.price!=0:
            print(f'-->price = {self.price} tk')
        self.cashback=int(self.price*(self.cashback/100))
        if self.cashback!=0:
            print(f'Buy now to get {self.cashback} tk cashback')
pkg = CellPackage(150, '6 GB', 99, 20, '7%', 7)
print('============= Package 1 =============')                
pkg2 = CellPackage(700, '35 GB', 700, 0, '10%', 30)
print('============= Package 2 =============')
pkg4 = CellPackage(120, '0 GB', 190, 0, '0%', 10)
print('============= Package 3 =============')
#https://docs.google.com/document/d/1jWyYz0JwV_PvVVpjSyKd0n_pMSlkOVmSFesMwzi2wGs/edit