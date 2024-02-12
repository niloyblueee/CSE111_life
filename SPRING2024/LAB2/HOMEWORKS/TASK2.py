def is_james_bond(numbers):
    count0=0
    count7=0
    for i in numbers:
        if i==0:
            count0+=1
        elif i==7 and count0==2:
            count7+=1    
    if count0==2 and count7==1:
        flag = True 
    else:
        flag = False    
    print(flag)    

is_james_bond( [1, 2, 4, 0, 0, 7, 5] )
is_james_bond( [1, 7, 2, 0, 4, 5, 0] )
is_james_bond( [1, 0, 2, 0, 4, 7, 5] )
