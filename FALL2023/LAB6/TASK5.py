class Student:
    brac=0
    total=0
    other=0
    def __init__(self,name,dpt,uni="BRAC University") :
        Student.total+=1
        self.name,self.dpt,self.uni=name,dpt,uni
        if uni=="BRAC University":
            Student.brac+=1
        else:
            Student.other+=1

    def individualDetail(self):   
        print(f'Name: {self.name}\nDepartment: {self.dpt}\nInstitution: {self.uni}') 


    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {Student.total}\nBRAC University Student(s): {Student.brac}\nOther Institution Student(s): {Student.other}")
    @classmethod
    def createStudent(cls,name,dpt,uni="BRAC University"):
        obj = cls(name,dpt,uni)         
        return obj

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
