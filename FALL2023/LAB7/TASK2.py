class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

#write your code here
class Cricket_Tournament(Tournament):
    def __init__(self,name="Default",number=0,type='No Type'):
        self.type,self.number_team=type,number
        super().set_name(name)
    def detail(self):
        return(f'Cricket Tournament Name: {self.get_name()}\nNumber of Teams: {self.number_team}\nType: {self.type}')    

class Tennis_Tournament(Tournament):
    def __init__(self,name="Default",number=0):
        self.number_players=number
        super().set_name(name)
        
    def detail(self):
        return(f'Tennis Tournament Name: {self.get_name()}\nNumber of Players: {self.number_players}')
     


ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())
