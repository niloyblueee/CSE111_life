s1=input('')
s2=''
upper_count=0
lower_count=0
for char in s1:
    if 'A'<=char<='Z':
        upper_count+=1
    elif 'a'<=char<='z':
        lower_count+=1
if upper_count>lower_count:
    for char in s1:
        if not 'A'<=char<='Z':
            s2+=chr(ord(char)-32)
        else:
            s2+=char 
else:
     for char in s1:
        if 'A'<=char<='Z':
            s2+=chr(ord(char)+32)
        else:
            s2+=char 
print(s2)       	



