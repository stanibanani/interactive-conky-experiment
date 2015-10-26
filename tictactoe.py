#!/usr/bin/python3
import sys, os
import pickle
# By Stanislav Puntjuk 2015-09-25

PATH = os.path.dirname(os.path.abspath(__file__))
GAMEFILE = PATH+"/game"

# Next 3 functions are for creating, laoding and saving a game.
def newGame():
    game_map = [[0,0,0],[0,0,0],[0,0,0]]
    turn = 'x'
    winner = None
    game = {"game_map":game_map,"turn":turn, "winner":winner}
    pickle.dump(game, open(GAMEFILE, "wb"))

def loadGame():
    game = pickle.load(open(GAMEFILE, "rb"))
    return game

def saveGame(game):
    pickle.dump(game, open(GAMEFILE,"wb"))

# These functions are for controlling the game.
def place(game, x, y):
    # Only place stuff if there is still no winner.
    if game["winner"] == None and game["game_map"][x][y] == 0:
            game["game_map"][x][y] = game["turn"]
            game = switchTurn(game)
            game["winner"] = checkWinner(game) # Check if there is a winner after every move.
            saveGame(game)

def switchTurn(game):
    if game["turn"] == "x":
        game["turn"] = "o"
    else:
        game["turn"] = "x"
    return game

def checkWinner(game):
    # returns the winner of the game

    # linearly check if %player% has won 
    def checkIter(row, col, row_inc, col_inc,player):
        game_map = game["game_map"]
        while(row < 3 and col < 3 and row >= 0 and col >= 0):
            if not game_map[row][col] == player:
                return False
            else:
                row+=row_inc
                col+=col_inc
        return True
    
    # returns the player that won the row, column or diagonal
    def checkBoth(row, col, row_inc, col_inc):
        if checkIter(row, col, row_inc, col_inc, 'x'):
            return 'x'
        elif checkIter(row, col, row_inc, col_inc, 'o'):
            return 'o'
        else:
            return None

    # check all rows and columns
    for i in range(3):
        winner = checkBoth(i,0,0,1)
        if not winner == None:
            return winner
      
        winner = checkBoth(0,i,1,0)
        if not winner == None:
            return winner

    # check diagonals
    winner = checkBoth(0,0,1,1)
    if not winner == None:
        return winner

    winner = checkBoth(0,2,1,-1)
    if not winner == None:
        return winner

    return None

def show(game):
    
    if not game["winner"] == None:
        print ("${color yellow}"+game["winner"]+" is the winner!")

    # print key indicators for rows and columns
    print ("${color }    1 2 3")
    
    # ugly hack for printing the column indicators
    i = 0

    for row in game["game_map"]:
        print("${color }", end="")
        if  i == 0:
            print ("Shf", end="|")
        elif i == 1:
            print ("Ctr", end="|")
        elif i == 2:
            print ("Alt", end="|")

        i+=1

        for el in row:
            if el == "x":
                print ("${color red}"+el, end="${color }|")
            elif el == "o":
                print ("${color blue}"+el, end="${color }|")
            else:
                print ("${color } ", end="|")
        print()
    

def main():

    command = sys.argv[1]
    # If argument "new" is passed create a new game file.
    if command == "new":
        newGame()
        return

    try:
        game = loadGame()
    except FileNotFoundError:
        newGame()
        game = loadGame()

    if command == "show":
        show(game)
    elif command == "place":
        x,y = int(sys.argv[2]), int(sys.argv[3])
        place(game, x, y)
    
if __name__ == "__main__":
    main()
