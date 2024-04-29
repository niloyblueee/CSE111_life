class PokemonBasic:

    def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type

    def get_type(self):
        return 'Main type: ' + self.type

    def get_move(self):
        return 'Basic move: ' + 'Quick Attack'

    def __str__(self):
        return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness


class PokemonExtra(PokemonBasic):
    def __init__(self,name,hp,weak,type,type2='',other_moves=''):
        super().__init__(name,hp,weak,type)
        self.type2,self.other_moves=type2,','.join(other_moves)

    def get_type(self):
        if self.type2!="":
            return f'Main type: {self.type},Secondary type: {self.type2}'
        else:
            return super().get_type()  

    def get_move(self):
        if self.other_moves!='':
            return f'Basic move: Quick Attack\nOther move: {self.other_moves}'
        else:
            return super().get_move()           

print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
