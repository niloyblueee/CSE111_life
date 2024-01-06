s1='baNgladEsh'
s2=''
ind1=0
ind2=0
while True:
    for char in range(len(s1)):
        if 'A'<=s1[char]<='Z':
            ind1=char
            break
    s1=s1[ind1+1:] 
    for char in range(len(s1)):
        if 'A'<=s1[char]<='Z':
            ind2=char
            break   
    s2+=s1[:ind2]
    s1=s1[ind2:] 
    break
if s2=='':
    s2='BLANK'
print(s2)         