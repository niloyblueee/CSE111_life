class Student:
    def __init__(self,name,cg,creds=9,dpt="CSE"):
        self.dpt=dpt
        self.name=name
        self.cg=cg
        self.creds=creds
        self.scholarship=''
    
    def checkScholarshipEligibility(self):
        if self.cg>=3.5 and self.creds>10:
            if self.cg>=3.7 :
                self.scholarship='Merit-based scholarship'
                print(f'{self.name} is eligible for {self.scholarship}')
            elif 3.5<=self.cg<3.7:
                self.scholarship='Need-based scholarship'
                print(f'{self.name} is eligible for {self.scholarship}')
        else:
            self.scholarship='No scholarship'
            print(f"{self.name} is not eligble for scholarship.")

    def showDetails(self):
        print(f'Name: {self.name}\nDepartment: {self.dpt}\nCGPA: {self.cg}\nNumber of Credoits: {self.creds}')
        print(f'Scholarship Status: {self.scholarship}')

print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
