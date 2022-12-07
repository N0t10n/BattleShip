from numpy import full

class BattleShip:

    def __init__(self, id=str, difficulty=None):
        self.id = id
        self.life = 20 # Total number of boat cells
        self.board = full((2, 10, 10), " ") # Empty board array
        self.boats = {4:1, 3:2, 2:3, 1:4} # Boat amount per type
        self.difficulty = difficulty # Just made for the machine