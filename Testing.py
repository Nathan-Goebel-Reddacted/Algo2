from Game import Game
from Glouton import Glouton
from Naif import Naif
from Top_down import Top_down
from Bottom_up import Bottom_up
import time
import os


def testManuel(game,path):
    start = time.perf_counter()
    game.AutoPlay(path)
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

def convertFile(filename):
    current_dir = os.path.dirname(__file__)
    full_path = os.path.join(current_dir, filename)
    T = []
    C = []

    with open(full_path, "r") as f:
        for line in f:
            if line.strip():
                t_val, c_val = map(int, line.strip().split())
                T.append(t_val)
                C.append(c_val)
    
    return [T,C]

def testTopDown(game):
    start = time.perf_counter()
    Top_down(game)
    end = time.perf_counter()
    duration = end - start
    print(f"TopDown Temps d'exécution : {duration:.6f} secondes")

def testBottomUp(game):
    start = time.perf_counter()
    Bottom_up(game)
    end = time.perf_counter()
    duration = end - start
    print(f"BottomUp Temps d'exécution : {duration:.6f} secondes")

if __name__ == "__main__":
    print("Test 1")
    print("******")
    Test1=Game([9,7,8,7,10,7],[2,1,1,4,4,2],-2,5)
    #resultat attendue 170pt avec Path = [0, 2, 4, 5]
    testManuel(Test1,[True,False,True,False,True,True])
    print("******")
    testGlouton(Test1)
    print("******")
    testNaif(Test1) 
    print("******")
    testTopDown(Test1)
    print("******")
    testBottomUp(Test1)

    print()
    print("------------------------------------------------")
    print()

    print("Test 2")
    print("******")
    Test2=Game([3,9,2,7,3,1],[2,2,5,4,2,1],2,-5)
    #resultat attendue 9pt avec Path = [0, 1, 4]
    testManuel(Test2,[True,True,False,False,True,False])
    print("******")
    testGlouton(Test2)
    print("******")
    testNaif(Test2)
    print("******")
    testTopDown(Test2)
    print("******")
    testBottomUp(Test2)

    print()
    print("------------------------------------------------")
    print()

    print("Test MP.txt")
    print("******")
    T,C=convertFile("MP.txt")
    Test3=Game(T,C,-3,7)
    testGlouton(Test3)
    print("******")
    #testNaif(Test3) 
    #testTopDown(Test3) #on ne fait pas les 2 car crash, ne sont pas conçus pour
    testBottomUp(Test3)      