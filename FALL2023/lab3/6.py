class Store:
    def __init__(self,balance):
        print('New Branch created!')
        self.balance=balance
        self.total_items=0
        self.items=''
        self.itemdetail={}
    def add_item(self,l1):
        name=l1[0]
        quantity=l1[1]
        buy=l1[2]
        sell=l1[3]
        self.items=name
        print('Item Added:',self.items)
        self.balance-=(quantity*buy)
        self.itemdetail[name]={'Stock':quantity,'buying_price':buy,'selling_price':sell}
        self.total_items+=1
    def sell_item(self,name,quantity):
        y=name
        x=self.itemdetail[name]
        stock=x['Stock']
        sell=x['selling_price']
        buy=x['buying_price']
        if quantity!=stock:
            print(f'Sorry! {y} is not available at your desired quantity. Currently we have {stock}') 
        else:
            z=stock-quantity
            self.balance+=quantity*sell
            self.itemdetail[name]={'Stock':z,'buying_price':buy,'selling_price':sell}
    def restock_item(self,name,quantity):
        x=self.itemdetail[name]
        self.balance-=quantity*x['buying_price']
        z=quantity
        sell=x['selling_price']
        buy=x['buying_price']
        self.itemdetail[name]={'Stock':z,'buying_price':buy,'selling_price':sell}  
        print(f'Restocked item: {name}\nCurrent Stock: {quantity}')     
    def viewAllItems(self):
        l=[]
        for i in self.itemdetail:
            l.append(i)
        s=','.join(l)   
        print(f'All items: {s}')
    def viewAllItemDetails(self):
        print(self.itemdetail)
        

print("==========================")
branch1 = Store(5000)
print(f"Current Balance: {branch1.balance}")
print(f"Total items: {branch1.total_items}")
branch1.viewAllItems()
branch1.viewAllItemDetails()
print("==========================")
print(f"Current Balance: {branch1.balance}")
branch1.add_item(["ChaCha Noodles", 10, 5, 8])
print(f"Current Balance: {branch1.balance}")
branch1.add_item(["Sparrow Shampoo", 5, 10, 20])
print(f"Current Balance: {branch1.balance}")
print("==========================")
branch1.viewAllItems()
print()
branch1.viewAllItemDetails()
print()
print("==========================")
print(f"Current Balance: {branch1.balance}\n")
branch1.sell_item("ChaCha Noodles", 15)
print(f"Current Balance: {branch1.balance}\n")
branch1.viewAllItemDetails()
print()
branch1.sell_item("ChaCha Noodles", 10)
print()
print(f"Current Balance: {branch1.balance}\n")
branch1.viewAllItemDetails()
print()
print("==========================")
print(f"Current Balance: {branch1.balance}\n")
branch1.restock_item("ChaCha Noodles", 5)
print()
branch1.viewAllItemDetails()
print()
print(f"Current Balance: {branch1.balance}\n")
print("==========================")


#https://docs.google.com/document/d/1jWyYz0JwV_PvVVpjSyKd0n_pMSlkOVmSFesMwzi2wGs/edit