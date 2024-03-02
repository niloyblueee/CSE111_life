class Student:
    idcount=0
    def __init__(self,name,dpt,age,cg):
        self.name,self.dpt,self.age,self.cgpa=name,dpt,age,cg
        Student.update_id()
    #classmethod for updating idcount
    @classmethod
    def update_id(cls):
        cls.idcount+=1
    #classmethod for forstring
    @classmethod
    def from_String(cls,all):
        name,dpt,age,cgpa=all.split("-")
        obj = cls(name,dpt,age,cgpa)
        return obj
    def  showDetails(self):
        print(f'ID: {Student.idcount}\nName: {self.name}\nDepartment: {self.dpt}\nAge: {self.age}\nCGPA: {self.cgpa}')   

s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails() 
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails() 


