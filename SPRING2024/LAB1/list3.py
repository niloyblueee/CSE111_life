l1=[]
l2=[]
x=input()
x=x.split()
y=input()
y=y.split()
for i in range(len(x)):
    l1.append(int(x[i]))
for j in range(len(y)):
    l2.append(int(y[j]))    
l3=[]  
for i in l1:
    for j in l2:
        l3.append(i*j)
print(l3)                    