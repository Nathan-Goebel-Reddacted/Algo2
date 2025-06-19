class Game:
    def __init__(self, T, C, A, B):
        # Vérifie les données
        if not isinstance(T, (list, tuple)) or not all(isinstance(t, int) for t in T):
            raise TypeError("T doit être une liste ou un tuple d'entiers (1D).")
        if not isinstance(C, (list, tuple)) or not all(isinstance(c, int) for c in C):
            raise TypeError("C doit être une liste ou un tuple d'entiers (1D).")
        if len(T) != len(C):
            raise ValueError("T et C doivent avoir la même longueur.")
        if not isinstance(A, int) or not isinstance(B, int):
            raise TypeError("A et B doivent être des entiers.")
        
        # Stocke les données
        self.T = T
        self.C = C
        self.A = A
        self.B = B
        self.LastChoice = None
        self.location = 0
        self.score = 0

    def GetLocation(self):
        return self.location

    def NextLocation(self):
        if self.location >= len(self.T) - 1:
            return None
        
        self.location += 1
        return self.location

    def Visite(self):

        if self.location >= len(self.T):
            return

        currentSymbole = self.C[self.GetLocation()]
        valeur = self.T[self.GetLocation()]

        if self.LastChoice == currentSymbole:
            self.score += self.A * valeur
        else:
            self.score += self.B * valeur

        self.LastChoice = currentSymbole
        self.NextLocation()

    def GetT(self):
        return self.T

    def GetC(self):
        return self.C
    
    def GetA(self):
        return self.A

    def GetB(self):
        return self.B

    def GetLastChoice(Self):
        return Self.LastChoice

    def PrintScore(self):
        print(f"Résultat = {self.score}")

    def GetScore(self):
        return self.score

    def AutoPlay(self, Turn):
        self.reset()
        if not isinstance(Turn, (list, tuple)) or not all(isinstance(turn, bool) for turn in Turn):
            raise TypeError("AutoPlay attend une liste de booléens (True/False) pour chaque emplacement.")
        if len(Turn) > len(self.C):
            raise ValueError("La longueur de Turn doit être inferieur ou égale à celle des emplacements.")

        for turn in Turn:
            if turn:
                self.Visite()
            else:
                self.NextLocation()
        
        return self.GetScore()
            

    def reset(self):
        self.LastChoice = None
        self.location = 0
        self.score = 0


def ConvertPath(BoolPath):
    path = []
    for index, value in enumerate(BoolPath):
        if value:
            path.append(index)
    return path

