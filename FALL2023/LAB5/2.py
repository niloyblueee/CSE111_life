class Student: #private
    def __init__(self,name,id,cg):
        self.__name=name
        self.__id=id
        self.__cgpa=cg
    def getname(self):
        return self.__name
    def getid(self):
        return self.__id
    def getcgpa(self):
        return self.__cgpa
    def setId(self,id):
        self.__id=id
class Department: #public
    def __init__(self,dpt):
        self.dpt=dpt
        self.students={'name':[],'id':[],"cgpa":[]}
    def findStudent(self,id):
        if id in self.students['id']:
            idx= self.students['id'].index(id)
            print(f'Student info:\nStudent Name: {self.students['name'][idx]}\nID: {id}\nCGPA:  {self.students['cgpa'][idx]}')
        else:
            print("Student with this ID doesn't exist, Please give a valid ID")
    def addStudent(self,*students):
        for i in students:
            self.students['name'].append(i.getname())
            if i.getid() not in  self.students['id']:   
                self.students['id'].append(i.getid())
            else:
                print('Student with the same ID already exists, Please try with another ID')
                break    
            self.students['cgpa'].append(i.getcgpa())         
            print(f'Welcome to {self.dpt} department, {i.getname()}')
    def details(self):
        print(f'Department Name: {self.dpt}\nNumber of student:{len(self.students['name'])}\nDetails of the students: ') 
        for i in range(len(self.students['name'])-1):
            print(f'Student name: {self.students['name'][i]} ID: {self.students['id'][i]} CGPA: {self.students['cgpa'][i]} ')          

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
