class Shopidify:
    def __init__(self,name='Guest') :
        self.name=name
        self.items={}
        self.tran=0
        if self.name=='Guest':
            print(f"Welcome to Shopidify")
        else:
            print(f"Welcome {self.name} to Shopidify")
    
    def add_to_cart(self,item,quan=1): 
        if type(item)==list:
            for idx in range(len(item)):
                if type(item[idx])==str:
                    self.items[item[idx]]=0
                else:
                    self.items[item[idx-1]]=item[idx]    
        else:
            self.items[item]=quan

    def display_cart(self):        
        print(f'Items in the cart for {self.name}:') 
        for i in self.items.keys():
            print(f'-{i}: {self.items[i]}x')
    def checkout(self):
        self.tran+=1
        print(f'Checkout completed for {self.name}')
    def display_history(self):
        print(f'Purchase history for {self.name}: Transaction {self.tran}:')
        for i in self.items.keys():
            print(f'-{i}: {self.items[i]}x')









guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")