class Teacher:     #THERE IS A MISTAKE IN THIS CODE [NO ENCAPSULATION IS USED] BUT I AM TOO BORED TO FIX IT
    def __init__(self,name,dpt):
        self.name=name
        self.dpt=dpt
        self.courses=[]
    def addCourse(self,c):
        if c.course not in self.courses:
          self.courses.append(c.course)    
    def printDetail(self):    
        print('====================================')
        print(f'Name: {self.name}\nDepartment: {self.dpt}\nList of courses')
        print('====================================')
        for i in self.courses:
            print(i)
        print('====================================')
        
class Course:
    def __init__(self,cname):    
        self.course=cname

t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")                          
c1 = Course("CSE 110 Programming Language I")                           
c2 = Course("CSE 111 Programming Language-II")                           
c3 = Course("CSE 220 Data Structures")                           
c4 = Course("CSE 221 Algorithms")                           
c5 = Course("CSE 230 Discrete Mathematics")                           
c6 = Course("CSE 310 Object Oriented Programming")                           
c7 = Course("CSE 320 Data Communications")                          
c8 = Course("CSE 340 Computer Architecture") 
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()

#https://docs.google.com/document/d/1-Nvkn__wzSLEBka94fKgJNdclgkHLcDUamKvi-nIBw0/edit
