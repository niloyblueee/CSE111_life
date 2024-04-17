class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
    def set_department(self, dept):
        self.__department = dept
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def detail(self):
        return 'Name: '+self.__name+' Department: '+self.__department


#write your code here
class BBA_Student(Student):
    def __init__(self,n='default'):
        self.set_name(n)
        self.set_department("BBA")




print(BBA_Student().detail())
print(BBA_Student('Humpty Dumpty').detail())
print(BBA_Student('Little Bo Peep').detail())