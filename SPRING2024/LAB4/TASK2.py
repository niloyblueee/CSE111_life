class Panda:
    def __init__(self,name,gen,age):
        self.name=name
        self.gender=gen
        self.age=age
        self.time=0
    def sleep(self,time):
        x=['Mixed Veggies','Eggplant & Tofu',
           'Broccoli Chicken','bamboo leaves'] 
        self.time=time
        if 3<=self.time<=5 :
            food=x[0]
        elif 6<=self.time<=8:
            food=x[1] 
        elif 9<=self.time<=11:
            food=x[2]
        else:
            food=x[3]
            return(f'{self.name} duration is unknown thus should have only {food}')
        return(f'{self.name} sleeps {self.time} hours daily and should have {food}')               


panda1 = Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female",3)
panda3 = Panda("Ming Ming", "Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep(13))
