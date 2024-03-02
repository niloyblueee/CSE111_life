class NikeBangladesh:
    Branches= [] 
    Stock= {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    Sold= 0
    
    def __init__(self,address):
        self.address=address
        NikeBangladesh.Branches.append(self.address)

    def restockProducts(self,dicc):
        for i in dicc.keys():
            NikeBangladesh.Stock[i]+=dicc[i]

    def details(self):
        print(f'Nike {self.address} outlet: \nProducts Currently Stocked:{NikeBangladesh.Stock}')

    def productSold(self,dicc):
        for i in dicc.keys():
            NikeBangladesh.Stock[i]-=dicc[i]
            NikeBangladesh.Sold+=dicc[i]
    @classmethod
    def status(cls):
        print("Nike Bangladesh Status: ")
        print(f'Branches Opened: {NikeBangladesh.Branches}')
        print(f'Currently Stocked \n{NikeBangladesh.Stock}\nSold: {NikeBangladesh.Sold}')


        
print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
