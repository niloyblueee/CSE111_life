class Foodie:
    def __init__(self,name) :
        self.name=name
        self.foods=[]
        self.cost=0
        self.items=0
    
    def order(self,*foods):
        quantitiy=0
        for i in foods:
            self.foods.append(i.split('-')[0])    
            quantitiy=int(i.split('-')[1])
            print(f'Ordered - {i.split('-')[0]}, quantity - {int(i.split('-')[1])}')
            print(f'price (per Unit) - {menu[i.split('-')[0]]}\nTotal price - {menu[i.split('-')[0]]*int(i.split('-')[1])}')
            self.cost+=menu[i.split('-')[0]]*quantitiy
            self.items+=1
    def show_orders(self):
        return(f'{self.name} has {self.items} item(s) in the cart\nItems: {self.foods}\nTotal spent: {self.cost}')
    
    def pay_tips(self,taka=0):
        self.tips=taka
        if self.tips==0:
            print('No tips to the waiter')
        else:
            self.cost+=self.tips
            print(f'Gives {self.tips}/- tips to the waiter')

menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}


f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())