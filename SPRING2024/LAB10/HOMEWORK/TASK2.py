class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here
class Player(SportsPerson):
    def __init__(self,team,name,role,goal,total):
        super().__init__(team,name,role)
        self.goal,self.total=goal,total
        self.earning_per_match= (self.goal*1000) + (self.total*10)
    def calculate_ratio(self):
        return (self.goal/self.total)
    def print_details(self):
        print(f'{super().get_name_team()}\nTeam Role: {self.role}\nTotal Goal: {self.goal}, Total Played: {self.total}\nGoal Ratio: {self.calculate_ratio()}\nMatch Earning: {self.earning_per_match}K')

class Manager(SportsPerson):
    def __init__(self,team,name,role,win):
        super().__init__(team,name,role)
        self.win=win
        self.earning_per_match=self.win * 1000

    def print_details(self):
        print(f'{super().get_name_team()}\nTeam Role: {self.role}\nTotal win: {self.win}\nMatch Earning: {self.earning_per_match}K')
    

player_one = Player('Al-Nassr', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
