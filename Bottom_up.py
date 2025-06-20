from Game import Game as GameClass
from Game import ConvertPath

class Bottom_up:
    def __init__(self, game: GameClass):
        if not isinstance(game, GameClass):
            raise TypeError("Instance de Game attendue.")
        
        self.game = game
        self.game.reset()

        T = self.game.GetT()
        C = self.game.GetC()
        a = self.game.GetA()
        b = self.game.GetB()
        n = len(T)

        etat = [(None, 0, [])]  

        for i in range(n):
            new_etat = []

            for pre_sym, current_score, current_path in etat:
                # visite pas
                path_novisit = current_path + [False]
                new_etat.append((pre_sym, current_score, path_novisit))

                # visite
                if pre_sym is not None and C[i] == pre_sym:
                    gain = a * T[i]
                else:
                    gain = b * T[i]

                new_score = current_score + gain
                path_visit = current_path + [True]
                new_etat.append((C[i], new_score, path_visit))

            best_scores = {}

            for sym, score, path in new_etat:  
                if sym not in best_scores or score > best_scores[sym][0]: 
                    best_scores[sym] = (score, path)

            etat = []
            for sym in best_scores:
                etat.append((sym, best_scores[sym][0], best_scores[sym][1]))

        best_score = None
        best_path = None
        for _, score, path in etat:
            if best_score is None or score > best_score:
                best_score = score
                best_path = path

        self.best_score = best_score
        self.bool_path = tuple(best_path)
        self.path = ConvertPath(best_path)

        print(f"ScoreMax = {self.best_score}")
        print(f"Path     = {self.path}")
