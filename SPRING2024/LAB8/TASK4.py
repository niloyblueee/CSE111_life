#task4
class Student:
  total=0
  brac=0
  other=0
  def __init__(self,name,dpt,uni='BRAC UNIVERSITY'):
    self.name,self.dpt,self.uni=name,dpt,uni
    Student.total+=1
    if self.uni=='BRAC UNIVERSITY':
      Student.brac+=1
    else:
      Student.other+=1
  def individualDetail(self):
         print(f'Name: {self.name}\nDepartment: {self.dpt}\nInstitution: {self.uni}')

  @classmethod
  def printDetails(cls):
    print(f'Total Student(s): {Student.total}\nBRAC University Student(s): {Student.brac}\nOther Institution Student(s): {Student.other}')

  @classmethod
  def createStudent(cls,name,dpt,uni='BRAC UNIVERSITY'):
    return cls(name,dpt,uni)







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
