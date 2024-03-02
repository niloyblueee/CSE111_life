class Travel:
    count=0
    def __init__(self,start,end):
        Travel.up_count()
        self.start,self.end=start,end
        self.Flight="1:00"
    def set_time(self,time):
        self.Flight=str(time)+":00" 
    def set_source(self,name):
        self.start=name
    def set_destination(self,name):
        self.end=name    
    def display_travel_info(self):
        return(f'Source: {self.start}\nDestination:{self.end}\nFlight Time:{self.Flight}')
    @classmethod
    def up_count(cls):
        Travel.count+=1

print("No. of Traveller =", Travel.count)
print("=======================")
t1 = Travel("Dhaka","India")
print(t1.display_travel_info())
print("=======================")
t2 = Travel("Kuala Lampur","Dhaka")
t2.set_time(23)
print(t2.display_travel_info())
print("=======================")
t3 = Travel("Dhaka","New_Zealand")
t3.set_time(15)
t3.set_destination("Germany")
print(t3.display_travel_info())
print("=======================")
t4 = Travel("Dhaka","India")
t4.set_time(9)
t4.set_source("Malaysia")
t4.set_destination("Canada")
print(t4.display_travel_info())
print("=======================")
print("No. of Traveller =", Travel.count)        