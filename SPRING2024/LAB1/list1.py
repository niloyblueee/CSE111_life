l1=[]
l2=[]
while True:
    x=input()
    if x == "STOP":
        break
    else:
        l1.append(int(x))
l1.sort()
l2=sorted(list(set(l1)))
for i in l2:
    print(i,'-',l1.count(i),'times')

