class Cakes:
    order_list={}
    feedbacks={}
    def __init__(self,flav,wt) :
        self.flav,self.wt=flav,wt
        self.sweet,self.cream='Moderate sugar','Whipped Cream'
        self.price=1.2*self.wt
        x=f'{self.flav} cake {self.wt} gm'
        if x not in Cakes.order_list.keys():
            Cakes.order_list[x]=1
        else:    
            Cakes.order_list[x]+=1

    def add_customization(self,sweet,cream):
        self.sweet,self.cream=sweet,cream

    def cake_details(self):
        print(f'Flavor: {self.flav} cake, Weight: {self.wt} gm\nSweetness: {self.sweet}, Cream Type: {self.cream}\nPrice: {self.price} Taka')


    @classmethod
    def give_feedbacks(cls,name,feed):
        if name not in cls.feedbacks.keys():
            cls.feedbacks[name]=[feed]
        else:
            cls.feedbacks[name].append(feed)
        print("Thanks for your valuable feedback!")    

    @classmethod
    def show_feedbacks(cls):
        print(cls.feedbacks)


class Cheese_Cakes(Cakes):
    def __init__(self,flav,wt,cake='baked'):
        super().__init__(flav,wt)
        self.price=1.5*self.wt
        self.cake=cake
        self.cream='Cream Cheese'
    def cake_details(self):
        print(f'Flavor: {self.flav} Cheese Cake, Weight: {self.wt} gm\nSweetness: {self.sweet}, Cream Type: {self.cream}\nCake Type: {self.cake}, Price: {self.price} Taka')

    def add_customization(self):
        print('Sorry! No customization available for cheese cakes')

    @classmethod
    def give_feedbacks(cls, name, feed):
        super().give_feedbacks(name, feed)
        print('You will get 10% discount for your next purchase!')




order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()
