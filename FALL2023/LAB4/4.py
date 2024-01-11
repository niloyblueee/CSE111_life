import math
class Sphere:
    def __init__(self,name,r=1,color='White'):
        self.name=name
        self.radius=r
        self.volume=(4/3*math.pi*self.radius**3)   
        self.color=color   
    def printDetails(self):
        print(f'Sphere ID:{self.name}\nColor:{self.color}\nVolume:{self.volume}')
    def merge_sphere(self,*sphere) :
        print('Spheres are being merged')
        for s in sphere:
            self.volume+=s.volume
            if self.color!=s.color:
                self.color='Mixed color'   

sphere1 = Sphere("Sphere 1")
print("1***************")
sphere1.printDetails()
print("2***************")
sphere2 = Sphere("Sphere 2", 3)
print("3***************")
sphere2.printDetails()
print("4***************")
sphere3 = Sphere("Sphere 3", 2)
print("5***************")
sphere3.printDetails()
print("6***************")
sphere3.merge_sphere(sphere1,sphere2)
print("7***************")
sphere3.printDetails()
print("8***************")
sphere4 = Sphere("Sphere 4", 5, "Purple")
print("9***************")
sphere4.merge_sphere(sphere3)
print("10***************")
sphere4.printDetails()
