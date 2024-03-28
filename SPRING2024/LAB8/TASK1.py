#task1
class Student:
  id_count=0
  def __init__(self,name,dpt,age,cg):
    self.name,self.dpt,self.age,self.cg=name,dpt,age,cg
    Student.id_count+=1
  def showDetails(self):
      print(f'ID: {Student.id_count}\nName: {self.name}\nDepartment: {self.dpt}\nAge: {self.age}\nCGPA: {self.cg}')
  @classmethod
  def from_String(cls,det):
    name,dpt,age,cg=det.split('-')
    age,cg=int(age),float(cg)
    obj = cls(name,dpt,age,cg)
    return obj

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
