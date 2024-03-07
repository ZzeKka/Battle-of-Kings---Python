from piece import *

class Player:
    
    def __init__(self, name, player_number):
        self.name = name
        if player_number == 1:
            self.king = King(0, 2, player_number) 
            self.barbarian = Barbarian(1, 1,  player_number)
            self.warrior = Warrior(1, 2, player_number)
            self.lancer = Lancer(1, 3, player_number)
        elif player_number == 2:
            self.king = King(7, 2, player_number)
            self.barbarian = Barbarian(6, 3, player_number)
            self.warrior = Warrior(6, 2, player_number)
            self.lancer = Lancer(6, 1, player_number)    
        
    