class abcTech:
    def __init__(self,name,desig,dpt):
        self.name=name
        self.designation=desig
        self.department=dpt
        self.frameworks=''
        self.skills=''
        self.total=0
        print(f'Welcome to abcTech, {self.name}!')
    def addProgrammingSkills(self,l1):
        if len(l1)==1:
            skills=l1[0]
            if self.skills=='':
                self.skills+=skills
            else:
                self.skills+=', '+skills
        else:
            if self.skills=='':
                for i in l1:
                    if i!=l1[-1]:
                        self.skills+=i+', '
                    else:
                        self.skills+=i 
            else:
                for i in l1:
                    if i!=l1[-1]:
                        self.skills+=', '+i+', '
                    else:
                        self.skills+=i 
    def addFrameworks(self,l1):
        if len(l1)==1:
            frame=l1[0]
            if self.frameworks=='':
                self.frameworks+=frame
            else:
                self.frameworks+=', '+frame
        else:
            if self.frameworks=='':
                for i in l1:
                    if i!=l1[-1]:
                        self.frameworks+=i+', '
                    else:
                        self.frameworks+=i 
            else:
                for i in l1:
                    if i!=l1[-1]:
                        self.frameworks+=', '+i+', '
                    else:
                        self.frameworks+=i 
    def printInfo(self):
        print(f'Name: {self.name}\nDesignation: {self.designation}\nDepartment: {self.department}\nProgramming skills: {self.skills}\nFrameworks: {self.frameworks}')
    def calculateSalary(self,tk,h):
        if h>144:
            self.total=(h-144)*800+tk
        else:
            self.total=tk
        return (self.total)    

print("-------------------------")
b1 =abcTech("Tamim Hasan", "Software Engineer", "Android Development")
print("-------------------------")
b1.addProgrammingSkills(["Java", "Python"])
b1.addProgrammingSkills(["Dart", "C++"])
b1.addFrameworks(["Express.js", "React"])
b1.printInfo()
print("-------------------------")
print(f"Your salary for this month is Tk. {b1.calculateSalary(45000, 156)}")
print("-------------------------")
print("-------------------------")
b2 =abcTech("Jahin Khandoker", "Senior Developer", "App Development")
print("-------------------------")
b2.addProgrammingSkills(["Java", "Dart", "Swift"])
b2.addFrameworks(["Flutter", "React Native"])
b2.addFrameworks(["Xamarin"])
b2.printInfo()
print("-------------------------")
print(f"Your salary for this month is Tk. {b2.calculateSalary(103000, 123)}")
print("-------------------------")
#https://docs.google.com/document/d/1jWyYz0JwV_PvVVpjSyKd0n_pMSlkOVmSFesMwzi2wGs/edit