def key_generator(*names):
    name_list=[name for name in names]
    encrypt=[]
    for name in name_list:
        temp=name[0].lower()
        for i in name[1:len(name)-1]:
            temp+=str(ord(i))
        temp+=name[-1].upper()
        encrypt.append(temp)
        temp=''
    print(encrypt)


key_list = key_generator ("Alex","Bob", "Trudy")