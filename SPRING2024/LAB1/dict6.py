s=input('')
s=s.upper()
d={1 :'.,?!:',
   2 :'ABC',
   3 :'DEF',
   4 :'GHI',
   5 :'JKL',
   6 :'MNO',
   7 :'PQRS',
   8 :'TUV',
   9 :'WXYZ',
   0 :' '}
out=''
for i in s:
    for keys in d.keys():
        if i in d[keys]:
            counter=0
            s2=d[keys]
            for ind in range(len(s2)):
                if s2[ind]==i:
                    counter=ind+1
            s2=''
            out+=str(keys)*counter
            break

print(out)