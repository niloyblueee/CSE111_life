class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area, self.name, self.height, self.base  = 0 , name, height, base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

#write your code here
class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0):
       super().__init__(name,height,base)
    def calcArea(self):
       return 0.5 * self.base * self.height
    def printDetail(self):
       return(f'Shape name: {self.name}\n{self.get_height_base()}\nArea: {self.calcArea()}')

class trapezoid(Shape):
    def __init__(self,name,height,base,side):
        super().__init__(name,height,base)
        self.area= side
    def calcArea(self):
        return ((self.base+self.area)/2*self.height)
    def printDetail(self,):
        return(f'Shape name: {self.name}\n{self.get_height_base()}, Side_A: {self.area}\nArea: {self.calcArea()}')

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
