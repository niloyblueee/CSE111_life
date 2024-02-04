d1={'key1':'value1',
    'key2':'value2',
    'key3':'value1'}
d2={}
for i in d1.values():
    d2[i]=0

for i in d2.keys():
    inp=[]
    for j in d1.keys():
        if d1[j]==i:
            inp.append(j)
            d2[i]=inp        
print(d2)        