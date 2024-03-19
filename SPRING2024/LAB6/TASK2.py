from os import name
class Student:
  def __init__(self,name,id,cg):
    self.name,self.id,self.cg=name,id,cg

  def setId(self,id):
    self.id=id
  #def printDetails(self):
    #print(f"Student info:\nStudent Name: {self.name}\nID: {self.Id}\nCGPA: {self.cg}")


class Department:
  def __init__ (self,name):
    self.name=name
    self.students={}

  def addStudent(self,*studs):
    for i in studs:
      if  i.id not in self.students.keys():
        self.students[i.id]=(i.name,i.cg)
        print(f"Welcome to {self.name} department, {i.name}")
      else:
        print("Student with the same ID already exists, Please try with another ID")

  def findStudent(self,id):
    if id in self.students.keys():
      print(f"Student info:\nStudent Name: {self.students[id][0]}\nID: {id}\nCGPA: {self.students[id][1]}")
    else:
      print("Student with this ID doesn't exist, Please give a valid ID")

  def details(self):
    print(f"Department Name: {self.name}\nNumber of student:{len(self.students.keys())}")
    print("Details of the students: ")
    for i in self.students.keys():
      print(f'Student name: {self.students[i][0]}, ID: {i}, cgpa: {self.students[i][1]}')


s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()

