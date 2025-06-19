from Game import Game as GameClass

class Glouton:
    def __init__(self,Game):
        if isinstance(Game,GameClass):
            self.Game = Game
        self.Game.reset()
        A,B= self.Game.GetA(),self.Game.GetB()
        path = []

        for index in range(len(self.Game.GetT())):
            if self.Game.GetLastChoice() == self.Game.GetC()[index]:
                Gain=A*self.Game.GetT()[index]
            else:
                Gain=B*self.Game.GetT()[index]
            if Gain > 0:
                self.Game.Visite()
                path.append(self.Game.GetLocation())
            else:
                self.Game.NextLocation()
        
        
        print(f"ScoreMax = {self.Game.GetScore()}")
        print(f"Path = {path}")
        
