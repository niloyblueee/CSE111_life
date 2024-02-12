import random
def playRockPaperScissors(rounds):
    me_score=0
    pc_score=0
    for i in range(rounds):
        me=input()
        pc=random.choice(['rock','paper','scissor'])
        print(f'Computer: {pc}')
        if me!=pc:
            if me=='rock' and pc=='scissor':
                me_score+=1
            elif  me=='rock' and pc=='paper':
                pc_score+=1
            elif  me=='scissor' and pc=='paper':
                me_score+=1
            elif  me=='scissor' and pc=='rock':
                pc_score+=1
            elif  me=='paper' and pc=='scissor':
                pc_score+=1
            elif  me=='paper' and pc=='rock':
                me_score+=1
    print (f"YOur Score:{me_score}\nComputer's Score:{pc_score}")
    if pc_score>me_score:
        print(f'Computer has won the game!')  
    else:
        print('You have won the game!')              

playRockPaperScissors(3)


