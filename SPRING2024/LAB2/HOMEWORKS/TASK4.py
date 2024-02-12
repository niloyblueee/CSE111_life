def username_generator(first='', last='', id='', middle=''):
    username=''
    id=str(id)
    username+=first[:3].upper()+middle+last[len(last)-3:]+'_'+id[len(id)-4:]
    return username

first_name, middle_name, last_name, student_id= input ("First Name:"), input("Middle Name:"), input ("Last Name:"), int (input ("Student ID:"))
print(username_generator (first_name, last_name, student_id))
print(username_generator(first_name, last_name, student_id, middle_name))