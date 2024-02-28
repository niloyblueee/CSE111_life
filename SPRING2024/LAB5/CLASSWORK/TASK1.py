class Student:
    def __init__(self,name,id,dpt="CSE"):
        self.name=name
        self.id=id 
        self.dpt=dpt
        self.effort=0
        self.suggestion=''
   
    def dailyEffort(self,time):
        self.effort=time
        if self.effort<=2:
            self.suugestion='Should give more effort!'
        elif self.effort<=4:
            self.suugestion='Keep up the good work!'
        else:
            self.suggestion='Excellent! Now motivate others.'
    def printDetails(self):
        print(f'Name: {self.name}\nID: {self.id}\nDepartment: {self.dpt}\nDaily Effort: {self.effort}\nSuggestion: {self.suggestion}')

harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()  
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
