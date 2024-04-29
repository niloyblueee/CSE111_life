import math
class TwoDVector:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    def add2DVectors(self, *vectors):
        for i in vectors:
            self.x += i.x
            self.y += i.y
    def print2DVector(self):
        if self.y >= 0:
            y = "+ "+str(self.y)    
        else:
            y = str(self.y)
        print(f"{self.x}i {y}j")

class ThreeDVector(TwoDVector):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def add3DVectors(self,*vectors):
        for i in vectors:
            self.add2DVectors(i)
            self.z += i.z
    
    def multiplyScalar(self,n):
        self.x*=n
        self.y*=n
        self.z*=n

    
    def calculateLength(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def print3DVector(self):
        if self.y >= 0:
            y = "+ "+str(self.y)
        if self.z >= 0 :
            z = "+ "+str(self.z)     
        else:
            y = str(self.y)
            z = str(self.z)
            print(f"{self.x}i {y}j {z}k")
            


TwoDV1 = TwoDVector(5, 6)
TwoDV2 = TwoDVector(3, 7)
TwoDV3 = TwoDVector(1, 8)
print("===============")
TwoDV1.add2DVectors(TwoDV2, TwoDV3)
TwoDV1.print2DVector()
print("===============")
ThreeDV1 = ThreeDVector(5, 6, 1)
ThreeDV2 = ThreeDVector(1, 9, -7)
ThreeDV3 = ThreeDVector(8, 2, 4)
print("===============")
ThreeDV1.add3DVectors(ThreeDV2,ThreeDV3)
ThreeDV1.print3DVector()
print("===============")
ThreeDV1.multiplyScalar(3)
ThreeDV1.print3DVector()
print("===============")
print(ThreeDV1.calculateLength())
