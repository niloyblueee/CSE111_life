class Player:
  total=0
  players=[]
  def __init__(self,name='',num=10,team=''):
    self.name,self.team,self.num=name,team,num
    Player.total+=1
    Player.players.append(self)
  def set_name(self,name):
    self.name=name

  def set_number(self,n):
    self.num=n
  def set_team(self,team):
    self.team=team
  def player_detail(self):
    return(f'Player Name: {self.name}\nJersey Number: {self.num}\nCountry: {self.team}')
  @classmethod
  def info(cls):
      x=[]
      print(f"Total number of players: {Player.total}\nPlayers enlisted so far:")
      for i in Player.players:
        x.append(i.name)
      print(", ".join(x))


print("Total number of players:", Player.total)
print("---------------------------")
p1 = Player()
p1.set_name("Neymar")
p1.set_team("Brazil")
print(p1.player_detail())
print('========================')
Player.info()
print("---------------------------")
p2 = Player("Ronaldo")
p2.set_number(7)
p2.set_team("Portugal")
print(p2.player_detail())
print('========================')
Player.info()
print("---------------------------")
p3 = Player("Messi")
p3.set_team("Argentina")
print(p3.player_detail())
print('========================')
Player.info()
print("---------------------------")
p4 = Player("Mbappe", 10, "France")
print(p4.player_detail())
print('========================')
Player.info()
