d1={}
while True:
    x=input()
    if x=="STOP":
        break
    else:
        if x not in d1.keys():
            d1[x]=1
        else:
            d1[x]+=1
d2=sorted(d1)
for i in d2:
    print(f'{i}-{d1[i]} times')