class StudentDatabase:
    def __init__(self, name,id):
        self.name, self.id=name, id
        self.grades={}
               
    def calculateGPA(self,l1,sem):
        temp=[]
        grades={}
        calculate=0
        for i in l1:
            temp.append(i.split(":")[0])
            cg=i.split(":")[1]
            calculate+=(float(cg)*3)
        calculate= (calculate / (len(l1)*3))    
        grades[tuple(temp)] = round(calculate,2)
        self.grades[sem] = grades 
        
    def printDetails(self):
        print(f'Name: {self.name}\nID: {self.id}')
        for i in self.grades.keys():
            print(f'Courses taken in {i}:')
            for j in self.grades[i].keys():
                for k in j:
                    print(k)
                
            print(f"GPA: {self.grades[i][j]}")
            
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0',
'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'],
'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7',
'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()

