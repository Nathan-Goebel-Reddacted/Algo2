# Top_down.py  — version pas-à-pas
from Game import Game as GameClass
from Game import ConvertPath

class Top_down:
    def __init__(self, game: GameClass) -> None:
        if not isinstance(game, GameClass):
            raise TypeError("Top_down attend une instance de Game.")

        self.game = game
        self.game.reset()

        T = self.game.GetT()        
        C = self.game.GetC()         
        A = self.game.GetA()          
        B = self.game.GetB()          
        n = len(T)                    

        memo = {}                    

        def dp(i, last_sym):

            cle = (i, last_sym)
            if cle in memo:
                return memo[cle]

            if i == n:
                return 0, []

            # visite pas
            score_skip, path_skip = dp(i + 1, last_sym)

            # visite
            if last_sym is not None and C[i] == last_sym:
                gain = A * T[i]
            else:
                gain = B * T[i]
            score_visit, path_visit = dp(i + 1, C[i])
            score_visit += gain

            if score_visit > score_skip:
                best_score  = score_visit
                best_path   = [True] + path_visit
            else:
                best_score  = score_skip
                best_path   = [False] + path_skip

            memo[cle] = (best_score, best_path)
            return best_score, best_path
        
        final_score, bool_path = dp(0, None)

        self.best_score = final_score
        self.bool_path  = tuple(bool_path)
        self.path       = ConvertPath(bool_path)

        print(f"ScoreMax = {self.best_score}")
        print(f"Path     = {self.path}")
