from Game import Game as GameClass
from Game import ConvertPath

class Naif:
    def __init__(self,Game):
        if isinstance(Game,GameClass):
            self.Game = Game
        Result=self.TakeATurn([])
        print(f"ScoreMax = {Result[0]}")
        path = ConvertPath(Result[1])
        print(f"Path = {path}")
        

    def TakeATurn(self,Path):
        #si terminer
        if len(Path)==len(self.Game.GetT()):
            Score = self.Game.AutoPlay(Path)
            return [Score,Path]
        #prochaine iteration
        PathTrue = Path + [True]
        PathFalse = Path + [False]
        ResultTrue=self.TakeATurn(PathTrue)
        ResultFalse=self.TakeATurn(PathFalse)

        #resoud l'iterration
        if ResultTrue[0]>ResultFalse[0]:
            return(ResultTrue)
        else:
            return(ResultFalse)
        
