s1='dean,tom'
s2=''
s3=''
out=''
for i in range(len(s1)):
    if s1[i]==',':
        s2=s1[:i]
        s3=s1[i+1:]
for char in s2:
    for char1 in s3:
        if char==char1:
            out+=char
if out=='':
    print('Nothing in Common')            
else:
    print(out)    