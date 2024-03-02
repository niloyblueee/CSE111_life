class Passenger:
    count=0
    def __init__(self,name):
        self.name=name
        self.bag_weight=0
        self.fare=450
        Passenger.up_passcount()

    def set_bag_weight(self,weight):
        self.bag_weight=weight
        if self.bag_weight<=20:
            self.fare=450
        elif 21<=self.bag_weight<=50:
            self.fare=500
        elif self.bag_weight>50:
            self.fare=550        

    def printDetail(self):
        print(f'Name: {self.name}\nBus Fare: {self.fare}')

    @classmethod
    def up_passcount(cls):
        Passenger.count+=1

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
