d={'key1': 'value1',
    'key2': 'value2',
   'key3': 'value1',
    'key4': 'value2',
     'key5': 'value3'}
d1={}
l=[]
for values in d.values():
    for keys in d.keys():
        if d[keys]==values:
            l.append(keys)
    d1[values]=l
    l=[]
print(d1)            