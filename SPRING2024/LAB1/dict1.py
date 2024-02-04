d1={'a': 100, 'b': 100, 'c': 200,'d': 300}
d2={'a': 300, 'b': 200, 'd': 400, 'e': 200}
d3={}
for i in d1.keys():
    if i in d2.keys():
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]    
for i in d2.keys():
    if i not in d3.keys():
        d3[i]=d2[i]
print(d3)        
values= [i for i in d3.values()] 
values=tuple(values)
print(f'Values: {(values)}')