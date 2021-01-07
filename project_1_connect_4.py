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

# import termcolor

def drawField(field):
    for row in range(6):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(7):
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    if column != 6:
                        print(field[practicalColumn][practicalRow],end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end="")
        else:
            print("-------------")

Player = 1
currentField = [[" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "]]

drawField(currentField)

while(True):
    print("Player turn: ",str(Player))
    MoveRow = int(input("Please enter de row between 1 and 3:\n"))-1
    MoveColumn = int(input("Please enter de column between 1 and 3:\n"))-1
    if Player == 1:
        #make move for Player 1
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "X"
            Player = 2
    else:
        #make move for Player 2
        if currentField[MoveColumn][MoveRow] == " ":
            currentField[MoveColumn][MoveRow] = "O"
            Player = 1
    drawField(currentField)