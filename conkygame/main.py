#!/usr/bin/python3
import sys, os
import pickle

PATH = os.path.dirname(os.path.abspath(__file__))

# A game is just a n*m plane with the player at a position
def loadSession(session):
    game = pickle.load(open(session,"rb"))
    return game

def printGame(game):
    for i in range(game["MAP_H"]):
        for j in range(game["MAP_W"]):
            if i == game["PLAYER_Y"] and j == game["PLAYER_X"]:
                print("o",end="") # dont print new line
            else:
                print(".", end="")
        print()

def moveDown(game):
    if game["PLAYER_Y"] > 0:
        game["PLAYER_Y"] -= 1

def moveUp(game):
    if game["PLAYER_Y"] < game["MAP_H"]:
        game["PLAYER_Y"] += 1

def moveLeft(game):
    if game["PLAYER_X"] > 0:
        game["PLAYER_X"] -= 1

def moveRight(game):
    if game["PLAYER_X"] < game["MAP_W"]:
        game["PLAYER_X"] += 1

def saveSession(session, game):
    pickle.dump(game, open(session, "wb"))

def main():
    # create new game session if argument "new" is passed
    if sys.argv[1] == "new":
        name = sys.argv[2]
        map_w = int(sys.argv[3])
        map_h = int(sys.argv[4])
        pickle.dump({"MAP_W":map_w, "MAP_H":map_h, "PLAYER_X":0,"PLAYER_Y":0}, open(name, "wb"))
        return

    # now the commands for an already existing game session
    session = PATH+"/"+sys.argv[1]
    command = sys.argv[2]

    GAME = loadSession(session)
    if command == "show":
        printGame(GAME)

    elif command == "left":
        moveLeft(GAME)
        saveSession(session,GAME)

    elif command == "right":
        moveRight(GAME)
        saveSession(session,GAME)

    elif command == "down":
        moveUp(GAME)
        saveSession(session,GAME)

    elif command == "up":
        moveDown(GAME)
        saveSession(session,GAME)

if __name__ == "__main__":
    main()
