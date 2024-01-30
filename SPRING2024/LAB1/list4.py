while True:
    x=input()
    if x=='STOP':
        break
    else:
        y=x.split()
        comprlist=[]
        for i in range(1,len(y)+1):
            comprlist.append(i)
        calclist=[]
        for i in y:
            calclist.append(int(i))
        n=1
        flag=True
        for i in range(len(calclist)):
            if calclist[i]!=calclist[-1]:
                dif=calclist[i]-calclist[i+1]
                if abs(dif) not in comprlist:
                    flag=False    
            else:
                break                 
        if flag==True:
            print("UB Jumper")
        else:
            print("Not UB Jumper")                            
