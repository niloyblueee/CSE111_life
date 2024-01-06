d1={ 'a': 100, 'b': 100, 'c': 200, 'd': 300} 
d2={'a': 300, 'b': 200, 'd': 400, 'e': 200 }
d3={}
sum=0
for keys in d1.keys():
    sum=0
    sum+=d1[keys]
    if keys in d2.keys():
        sum+=d2[keys]
        d3[keys]=sum
    else:
        d3[keys]=d1[keys]
for keys2 in d2.keys():
    if keys2 not in d1.keys():
        d3[keys2]=d2[keys2]        
tup=tuple(sorted(set((d3.values()))))
print(d3)
print('Values:',tup)