#task6 try 2
#task6
def capitalizer(para):

  fixed=''
  for idx in range(len(para)):
      if idx == 0 and para[idx] in 'abcdefghijklmnopqrstuvxyz':
        fixed+= para[idx].upper()
        continue
      elif (para[idx-2] == '.' and para[idx-1] ==' ') or (para[idx-2] =='?' and para[idx-1] == ' ') or (para[idx-2] =='!' and para[idx-1] ==' '):
        fixed+=para[idx].upper()
        continue
      elif para[idx]=='i' and para[idx+1] not in 'abcdefghijklmnopqrstuvxyz' and para[idx-1] not in 'abcdefghijklmnopqrstuvxyz' :
        fixed+='I'
      else:
        fixed+=para[idx]
  print(fixed)
capitalizer("my favourite animal is a dog. a dog has a sharp teeth so that it can eat flesh very easily. do you know my pet dog's name? i love my pet very much, do i?")
