class Team: #private
    def __init__(self,name=""):
        self.__name=name
        self.__players=[]
    def setName(self,name):
        self.__name=name
    def addPlayer(self,other):
        self.__players.append(other.name)
    def printDetail(self):
        print(f'=====================\nTeam: {self.__name}\nList of Players:\n{self.__players}\n=====================') 


class Player:
    def __init__(self,name):
        self.name=name

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
