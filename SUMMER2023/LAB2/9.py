class buttons:
    def __init__(self,word,spaces,borders):
        self.name=word
        self.spaces=spaces
        self.borders=borders
        self.calc=1+self.spaces+len(self.name)+self.spaces+1
        print(f'{self.name} Button specifications:\nButton name: {self.name}\nNumber of the border characters for the top and the bottom: {self.calc}\nNumber of spaces between the left side border and the first character of the button name: {self.spaces}\nNumber of spaces between the right side border and the last character of the button name: {self.spaces}\nCharacters representing the borders: {self.borders}')     
        print(self.borders*self.calc)
        print(self.borders,end='')
        print(' '*self.spaces,end='')
        print(self.name,end='')
        print(' '*self.spaces,end='')
        print(self.borders)  
        print(self.borders*self.calc)


#Write your class code here

word = "CANCEL"  
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
#https://docs.google.com/document/d/1oA_wx5IeniGbiUn2gPXymXpKAADH-TrK/edit