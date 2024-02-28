class Department:
    def __init__(self,dpt='Che Department',sections=5):
        self.dpt,self.sections=dpt,sections
        print(f'The {self.dpt} has {self.sections} sections.')
        self.studs=0

    def add_students(self,*studs):
        tempSUM=0
        if len(studs)==self.sections:
            for i in studs:
                tempSUM+=i
            self.studs=tempSUM    
            avg=self.studs/self.sections        
            print(f'The ChE Department has an average of {avg} students in each section.')
        else:   
            print(f"The MME Department doesn't have {len(studs)} sections.")
    
    def merge_Department(self,*dpts):
        for i in dpts:
            print(f'{i.dpt} is merged to {self.dpt}.')
            
            self.studs+=i.studs
        avg=self.studs/self.sections
        return (f'Now the {self.dpt} has an average of {avg} students in each section.') 

d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))
    