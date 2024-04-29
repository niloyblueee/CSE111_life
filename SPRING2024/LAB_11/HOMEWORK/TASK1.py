class Employee: #bap
    def __init__(self,name,id,dpt) :
        self.name,self.id,self.dpt=name,id,dpt
        self.salary=30000
        self.type=''
    def employeeDetails(self): 
        if self.type == '':
            print(f'Name: {self.name}, Dept {self.dpt}\nEmployee id: {self.id}, Salary: {self.salary}')
        else:
            print(f'Name: {self.name}, Dept {self.dpt}\nEmployee id: {self.id}, Salary: {self.salary}\nEmployee Type: {self.type}')
        
    def workDistribution(self,distri):
        if distri!= "Human Resource":
            print('Collect work distribution loads from the HR department.')
        else:
            print('Collect work distribution details from the manager.')

    def increment(self):
        self.salary+= self.salary*.1

    def set_salary(self,n):
        self.salary=n

class Foreign_employee(Employee): #beta1
    def __init__(self,name,id,dpt):
        super().__init__(name,id,dpt)
        self.type="Foreign"
    def increment(self):
        super().set_salary(30000)
        self.salary+= self.salary*.15

class Part_time_employee(Employee): #beta2
    def __init__(self,name,id,dpt):
        super().__init__(name,id,dpt)
        self.type="Part Time"
    def increment(self):
        super().set_salary(15000)
        print('Sadly, there is no increment for the part time employees')

print("1------------------------------------------")
emp1=Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp=Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp=Part_time_employee("Asif", 210, "Sales")
p2_emp=Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()
