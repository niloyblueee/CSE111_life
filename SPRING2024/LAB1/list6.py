y=input()
y=y.split()
n_member,k_time=int(y[0]),int(y[1])
members=[]
teammembers=3
maxpart=5
temp1=0
out=0
x=input()
x=x.split()
for i in x:
    members.append(int(i))
for calc in members:
    if calc+k_time<=maxpart:
        temp1+=1
    if temp1==teammembers:
        out+=1
        temp1=0
print(out)        
