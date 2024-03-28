class Passenger:
    count=0
    def __init__(self,name):
        self.name,self.bag,self.fare=name,0,0
        Passenger.count+=1
    def set_bag_weight(self,a):    
        self.bag=a
        if self.bag>20 and self.bag<=50:
            self.fare=450+50
        elif self.bag>50:
            self.fare=450+100
        else:
            self.fare=450        

    def printDetail(self):
        print(f'Name: {self.name}\nBus Fare: {self.fare} taka')

print("Total Passenger:", Passenger.count)
p1 = Passenger("Jack")
p1.set_bag_weight(90)
p2 = Passenger("Carol")
p2.set_bag_weight(10)
p3 = Passenger("Mike")
p3.set_bag_weight(25)
print("=========================")
p1.printDetail()
print("=========================")
p2.printDetail()
print("=========================")
p3.printDetail()
print("=========================")
print("Total Passenger:", Passenger.count)
