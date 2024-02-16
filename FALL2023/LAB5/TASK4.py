class Usis:
    def __init__(self):
        self.flag=False
        print("USIS is ready to use!")
    
    def login(self,student):
        if student.email==None or  student.password==None:  
            print('Email and password need to be set.')
        else:
            print('Login successful!')
            self.flag=True
    def advising(self,student,*courses):
        if self.flag==True:
            if len(courses)==0:
                print("You haven't selected any courses.")
            elif len(courses)>3 or len(student.course)==3:
                print("You need special approval to take more than 3 courses.")    
            else:
                for i in courses:
                    student.course.append(i)
                
                print("Advising successful!")
        else:
                print("Please login to advise courses!")    
    def individualDetails(self,student):
        x=', '.join(student.course)
        return(f"Name: {student.name}\nID: {student.id}\nDepartment: {student.department}\nAdvised courses: {x}")
class Student:
    def __init__(self,name,id,dpt):
        self.name=name
        self.id=id
        self.department=dpt
        self.email=None
        self.password=None
        self.login=None
        self.course=[]

        print('Student object is created!')


rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
print(usis_obj.individualDetails(rakib))
print("10***********************")
usis_obj.advising(rakib, "CSE111")
