x=input("").lower()
d1={}
for i in x:
    if i != " ":
        if i not in d1.keys():
           d1[i]=1
        else:
            d1[i]+=1   
print(d1)        
