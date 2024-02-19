class box:
    def __init__(self,l1):
        print('Creating a Box!')
        self.height=l1[0]
        self.width=l1[1]
        self.breadth=l1[2]
        self.volume=self.height*self.width*self.breadth
        

print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")

#=============================
one = (b3 == b2)
print(one) #will be true cz the memory location of both objects are same
b3.width = 100
print(b3.width)#we assigned new values on previous line ,so value of both objects width are changed
two = (b3 == b2) ##will be true cz the memory location of both objects are same,just the value in the object has changed doesnt affect the location

