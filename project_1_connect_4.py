"""

programmer: Felix Perez

Project #1: develop Connect 4 game

Rules:

    - 2 Players.
    - Pieces X and O instead, red and black.
    - Board 7 column x 6 rows.
    - Game by turns.
    - The goal is to get 4 pieces of your own color in a row.
    - Row can be horizontaly, verticaly, or angle.

"""

import termcolor

def drawField(field):
    for vertical in range(6):
        for horizontal in range(7):
                if horizontal < 6:
                    if field[int(vertical)][int(horizontal)] == 'X':
                        print(termcolor.colored(field[int(vertical)][int(horizontal)],'red'),' | ',end="")
                    else:
                        print(termcolor.colored(field[int(vertical)][int(horizontal)],'blue'),' | ',end="")
                else:
                    if field[int(vertical)][int(horizontal)] == 'X':
                        print(termcolor.colored(field[int(vertical)][int(horizontal)],'red'))
                    else:
                        print(termcolor.colored(field[int(vertical)][int(horizontal)],'blue'))
                    print("--------------------------------")

Player = 1
currentField = [[" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "]]
autoVertical = [5,5,5,5,5,5,5]
drawField(currentField)

while(True):
    print("Player turn: ",str(Player))
    SelectHorizontal = int(input("Please enter de column between 1 and 7:\n"))-1
    SelectVertical = autoVertical[SelectHorizontal]
    if Player == 1:
        #make move for Player 1
        if currentField[SelectVertical][SelectHorizontal] == " ":
            currentField[SelectVertical][SelectHorizontal] = "X"
            Player = 2
    else:
        #make move for Player 2
        if currentField[SelectVertical][SelectHorizontal] == " ":
            currentField[SelectVertical][SelectHorizontal] = "O"
            Player = 1
    if autoVertical[SelectHorizontal] != 0:
        autoVertical[SelectHorizontal] -=1
    drawField(currentField)