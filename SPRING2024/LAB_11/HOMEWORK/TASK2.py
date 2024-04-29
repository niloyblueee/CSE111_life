class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
        
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"



class ScienceExam(Exam) :
    def __init__(self,marks,time,*parts):
        super().__init__(marks)
        subs=[]
        for i in parts:
            subs.append(str(i))
        self.time,self.new_subs=time,subs
    
    def __str__(self) :
        return (f'Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.new_subs)+2}')

    def examSyllabus(self):   
        x= super().examSyllabus()
        return str(x)+' , '+ ' , '.join(self.new_subs)
    
    def examParts(self):
        x=super().examParts()
        for idx in range(len(self.new_subs)):
            if idx==0:
                x+= f'Part {idx+3} - {self.new_subs[idx]}'
            else:
                x+= f'\nPart {idx+3} - {self.new_subs[idx]}'
        return x    
             

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================') 
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())
