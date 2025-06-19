from Game import Game
from Glouton import Glouton
from Naif import Naif
from Bottom_up import Bottom_up
from Top_down import Top_down
import time


def testManuel(game):
    start = time.perf_counter()
    game.AutoPlay([True,False,True,False,True,True])
    game.PrintScore()
    end = time.perf_counter()
    duration = end - start

    print(f"Manuel Temps d'exécution : {duration:.6f} secondes")

def testGlouton(game):
    start = time.perf_counter()
    Glouton(game)
    end = time.perf_counter()
    duration = end - start

    print(f"Glouton Temps d'exécution : {duration:.6f} secondes")

def testNaif(game):
    start = time.perf_counter()
    Naif(game)
    end = time.perf_counter()
    duration = end - start

    print(f"Naif Temps d'exécution : {duration:.6f} secondes")










if __name__ == "__main__":
    Test1=Game([9,7,8,7,10,7],[2,1,1,4,4,2],-2,5)
    #resultat attendue 170pt avec Path = [0, 2, 4, 5]
    testManuel(Test1)   #temps= .000 077 s
    testGlouton(Test1)  #temps= .000 113 s
    testNaif(Test1)     #temps= .000 251 s  chemin optimal trouver
