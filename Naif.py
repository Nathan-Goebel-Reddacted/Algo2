from Game import Game

class Naif:
    def __init__(self,Game):
        if isinstance(Game,Game):
            self.Game = Game
        
