class box:
    def __init__(self,l1):
        print('Creating a Box!')
        self.height=l1[0]
        self.width=l1[1]
        self.breadth=l1[2]
        self.volume=self.height*self.width*self.breadth
        print(f'volume of the box is {self.volume} cubic units')
   
print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
#https://docs.google.com/document/d/1oA_wx5IeniGbiUn2gPXymXpKAADH-TrK/edit