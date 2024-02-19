#4
class Student:
  def __init__(self,name,cgpa,coursesN):
    self.name=name
    self.cgpa=cgpa
    self.courses_taken=coursesN
    if self.cgpa<2.0:
      self.student_status='Probation'
    else:
      self.student_status='Regular'

    if self.student_status=='Probation' and 1<=self.courses_taken<=2:
      self.advising_status='Approved'
      print(f'Study hard this time,{self.name}')
    elif self.student_status=='Regular' and 3<=self.courses_taken<=5:
      self.advising_status='Approved'
    elif self.student_status=='Probation' and not 1<=self.courses_taken<=2:
      self.advising_status='Denied'
      self.courses_taken=0
      print(f'Sorry, {self.name}, you are on {self.student_status} and cannot take more than 2 courses.')

    elif self.student_status=='Regular' and not  3<=self.courses_taken<=5:
      self.advising_status='Denied'
      self.courses_taken=0
      print(f'Hello {self.name}, you are a {self.student_status} student and have to take between 3 to 5 courses')


s1 = Student("Clark", 3.45, 4)
print(f"Name: {s1.name}\nCGPA: {s1.cgpa}\nCourses Taken: {s1.courses_taken}")
print(f"Student Status: {s1.student_status}\nAdvising Status: {s1.advising_status}")
print("--------------------------------------------------------------------------------")
s2 = Student("Barry", 1.93, 2)
print(f"Name: {s2.name}")
print(f"Student Status: {s2.student_status}\nAdvising Status: {s2.advising_status}")
print("--------------------------------------------------------------------------------")
s3 = Student("Diana", 2.91, 2)
print(f"Advising Status: {s3.advising_status}\nCourses Taken: {s3.courses_taken}")
print("--------------------------------------------------------------------------------")
s4 = Student("Bruce", 1.52, 5)
print(f"Advising Status: {s4.advising_status}\nCourses Taken: {s4.courses_taken}")