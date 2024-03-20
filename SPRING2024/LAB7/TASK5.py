class BracuStudent:
  def __init__(self,name,adrs):
    self.name,self.home=name,adrs
    self.busPass=False


  def get_pass(self):
    self.busPass=True
  def show_details(self):
    print(f'Student Name: {self.name}\nLives in {self.home}\nHave Bus Pass? {self.busPass}')

class BracuBus:
  def __init__(self,destination,cap=2):
    self.destination,self.cap=destination,cap
    self.passengers=[]
    self.temp=cap
  def board(self,*i):
    if len(i)==0:
      print('No passengers!')
    else:
      for other in i:
        if  other.busPass==True and self.destination==other.home and self.temp!= 0:
          self.passengers.append(other.name)
          self.temp-=1
          print(f'{other.name} boarded the bus')
        elif other.busPass==False  :
          print("You don't have a bus pass!")
        elif  self.destination!=other.home:
          print('You got on the wrong bus!')
        elif     self.temp== 0:
          print('Bus is full!')

  def show_details(self):
    print(f'Bus Route: {self.destination}\nPassengers Count: {len(self.passengers)} (Max: {self.cap})\nPassengers On Board: {self.passengers}')


st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
