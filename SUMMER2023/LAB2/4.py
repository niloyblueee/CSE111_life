class Pokemon:
    def __init__(self,p1,p2,p1pow,p2pow,combo):
        self.pokemon1_name=p1
        self.pokemon2_name=p2
        self.pokemon1_power=p1pow
        self.pokemon2_power=p2pow
        self.damage_rate=combo

team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name, team_bulb.pokemon2_power)
pika_combined_power = (team_bulb.pokemon1_power + team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', pika_combined_power)
#https://docs.google.com/document/d/1oA_wx5IeniGbiUn2gPXymXpKAADH-TrK/edit