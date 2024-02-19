class Order:
  def __init__(self,menuDict,orders):
    self.menu=menuDict
    orderDetails={}
    self.items=[]
    temp=orders.split(",")
    for i in temp:
        x=str(i).lstrip()
        y=x.split("-")
        orderDetails[y[0]]=int(y[1])
        
    for i in orderDetails.keys():
        self.items.append(i)
        self.items.append(orderDetails[i])
        self.items.append(self.menu[i]*orderDetails[i])
           
# Write your class code here
menu = {
    'Chicken_Cheeseburger' : 249,
    'Mega_Cheeseburger' : 289,
    'Fries' : 139,
    'Hot_Wings' : 99,
    'Rice_Bowl' : 299,
    'Soft_Drinks' : 50
}

order1 = Order(menu, "Chicken_Cheeseburger-2, Fries-3, Soft_Drinks-3")
print(order1.items)
print()

print('-'*35)
print('Item           x Quantity :   Price')
print('--------------   --------   -------')

index = 0
total = 0
while index < len(order1.items):
  item = order1.items[index]
  quantity = order1.items[index+1]
  price = order1.items[index+2]

  print(f'{item:20} x {quantity:2} : {price:7.2f}')
  total += price
  index += 3 # Going to next item

print('-'*35)
print(f'Total:                      {total:7.2f}')
print('-'*35)