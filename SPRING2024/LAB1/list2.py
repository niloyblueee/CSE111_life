maincalc=0
tempcalc=0
mainlist =[]
templist=[]
for lnum in range(int(input())):
        x=input()
        templist=x.split()
        for i in templist:
            tempcalc+=int(i)
        if tempcalc>maincalc:
            mainlist=[]
            for i in templist:
                mainlist.append(int(i))        
        maincalc=tempcalc
        templist=[]
        tempcalc=0
print(maincalc,mainlist,sep='\n')
