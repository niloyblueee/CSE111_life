class  KK_tea:
    sell={}
    def __init__(self,price,quant=50,name="Regular"):
        Main= "KK "+name+" Tea"
        self.name,self.price,self.quant=Main,price,quant
        self.weight=2*self.quant
        self.sold=False
        KK_tea.sell[self.name] = 0   

    def product_detail(self):
        print(f'Name: {self.name}, Weight: {self.weight}\nTea Bags: {self.quant}, Price: {self.price}\nStatus: {self.sold}')

    @classmethod
    def update_sold_status_regular(cls,*items):
        for i in items:
            i.sold=True
            KK_tea.sell[i.name] +=1
    @classmethod
    def total_sales(cls):
       print(f'Total sales: {cls.sell}')
               

class KK_flavoured_tea(KK_tea):
    def __init__(self,name,price,quant):
        super().__init__(price,quant,name)
    @classmethod
    def update_sold_status_flavoured(cls,*items):
        for i in items:
            i.sold=True
            KK_tea.sell[i.name] +=1

t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()



        