class StudentDatabase:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.gpa=[]
        self.course=[]
        self.directory={}
        self.sem=[]
        self.grades={}
    def calculateGPA(self,l1,sem):
        self.sem.append(sem)
        course=[]
        directory={}
        temp=0
        for i in l1:
            for j in range(len(i)):
                if i[j]==':':
                    course.append(i[:j])
                    gpa=float(i[j+2:])
                    break
            temp+=gpa*3
        tempgpa=temp/(len(course)*3)      
        self.gpa.append(tempgpa)    
        self.course.append(course)
        tempdirect={tuple(course):tempgpa}
        self.directory[sem]=tempdirect
        self.grades=self.directory

    def printDetails(self):
        print(f'Name: {self.name}\nID: {self.id}')
        for i in range(len(self.directory)):
            print(f'Courses taken in {self.sem[i]}:')
            for j in self.course[i]:
                print(j)
            print('GPA: ',self.gpa[i])
#write your code above
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()

#