inp1=input()
inp2=input()
d1={}
d2={}
for i in inp1:
    if i not in d1.keys():
        d1[i]=1
    else:
        d1[i]+=1
for j in inp2:        
    if j not in d2.keys():
        d2[j]=1
    else:
        d2[j]+=1 
flag=True
for checking in inp2:
   if d1[checking]!=d2[checking]:
       flag=False
if flag==True:
    print("Those strings are anagrams.")
else:    
    print("Those strings are not anagrams.")