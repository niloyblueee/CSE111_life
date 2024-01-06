s1=input('')
s2=0
s3=0
for char in s1:
    if '1'<=char<='9' :
        s2=1
    elif ('a'<=char<='z' or 'A'<=char<='Z'):
        s3=1 
    if '1'<=char<='9' and ('a'<=char<='z' or 'A'<=char<='Z'):
        s2=2
if s2==1 and s3!=1:
    print('number')
elif s3==1 and s2!=1:
    print('words')
elif s2==1 and s3==1:
    print('mixed')

            



