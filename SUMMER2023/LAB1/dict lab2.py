l=[]
while True:
    s=input('')
    if s=='STOP':
        break
    else:
        l.append(s)
l.sort()
l2=set(l)
d={}
n=1
for num in l2:   
    a=l.count(num)
    d[num]=a
sorted(d)
print(d)