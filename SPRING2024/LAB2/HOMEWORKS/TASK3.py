def assign_students_to_sections(sections,*students):
    output={}
    num_sections=len(sections)
    for i in sections:
        output[i]=[]
    for name in students:
        ascii=0
        for i in name:
            ascii+=ord(i)
        idx_of_sec=ascii%num_sections
        output[sections[idx_of_sec]].append(name)
    print(output)

assign_students_to_sections ('ABCDE', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace')


