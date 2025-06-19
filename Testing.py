from Game import Game
from Glouton import Glouton
from Naif import Naif
from Bottom_up import Bottom_up
from Top_down import Top_down
import time


def testManuel():
    #tester un game manuel resultat esperer 170
    start = time.perf_counter()
    Test1=Game([9,7,8,7,10,7],[2,1,1,4,4,2],-2,5)
    Test1.AutoPlay([True,False,True,False,True,True])
    Test1.PrintScore()
    end = time.perf_counter()
    duration = end - start

    print(f"Temps d'exécution : {duration:.6f} secondes")
    #sur mon ordi temps moyent < 0.0001s


if __name__ == "__main__":
    testManuel()