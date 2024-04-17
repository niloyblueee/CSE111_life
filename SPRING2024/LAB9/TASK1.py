class NikeBangladesh:
  branch=[]
  sold=0
  total_stock={}
  def __init__(self,name):
    self.outlet=name
    NikeBangladesh.branch.append(self.outlet)
    self.stock={}
    self.sold=0
  def details(self):
    print(f'Nike {self.outlet} outlet:\nProducts currently stocked:\n{self.stock}\nSold: {self.sold}')

  def restockProducts(self,dic):
    #{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
    self.stock=dic
    for i in dic.keys():
      if i not in NikeBangladesh.total_stock.keys():
        NikeBangladesh.total_stock[i]=dic[i]
      else:
        NikeBangladesh.total_stock[i]+=dic[i]
  def productSold(self,dic):
    for i in dic.keys():
      self.stock[i]-=dic[i]
      NikeBangladesh.total_stock[i]-=dic[i]
      self.sold+=dic[i]
    NikeBangladesh.sold+=self.sold

  @classmethod
  def status(cls):
    print(f'Nike Bangladesh Status:\nBranches Opened:  {NikeBangladesh.branch}\nCurrently Stocked\n{NikeBangladesh.total_stock}\nSold: {NikeBangladesh.sold}')

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

