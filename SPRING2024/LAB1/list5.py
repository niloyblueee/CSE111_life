x=input()
y=''
smchr=''
bgchr=''
oddnmbr=''
evennmbr=''
for i in x:
    if 'a'<=i<='z':
        smchr+=i
    elif "A"<=i<="Z":
        bgchr+=i    
    elif i in '13579':
        oddnmbr+=i
    else:
        evennmbr+=i    
z=sorted(smchr)+sorted(bgchr)+sorted(oddnmbr)+sorted(evennmbr)
for i in z:
    y+=i
print(y)        