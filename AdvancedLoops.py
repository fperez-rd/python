"""
programmer: Felix Perez
Homework Assignment #6: Advanced Loops

*This program draw on screen a empty board for tic tac toe game.

rows * columns

"""

def TicTacToeBoard(rows,columns):
    rows_int = int(rows)
    columns_int = int(columns)
    output = True

    if rows_int <= 32 and columns_int <= 133:
        for r in (range(0,rows_int)):
            if r%2 == 0:
                for c in (range(1,columns_int+1)):
                    if c%2 == 1:
                        if c != columns_int:
                            print(" ",end="")
                        else:
                            print(" ")
                    else:
                        print("|",end="")
            else:
                print("-"*(columns_int))
    else:
        output = False
        
    return output

TicTacToeBoard(60,200)