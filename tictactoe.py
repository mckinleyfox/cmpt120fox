# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: McKinley Fox
# Created: 2019-04-08

symbol = [ " ", "x", "o" ]
def printRow(row):
    # initialize output to the left border
    output = "|"
    # for each square in the row...
    for i in range(3): 
        # add to output the symbol for this square followed by a border 
        output = output + " " + symbol[row[i]] + " |"
        # print the completed output for this row
    print(output)

def printBoard(board):
    print("+-----------+")# print the top border
    for i in range(3):# for each row in the board... # print the row
        printRow(board[i])
        print("+-----------+")

def players(player1, player2):
    player1 == "x"
    player2 == "o"

def markBoard(board, row, col, player):
    if board[row][col] == 0:# check to see whether the desired square is blank
        board[row][col] = player# if so, set it to the player number
    else:
        print("This spot is already filled. Choose a new spot.")

def getPlayerMove():
    row = int(input("Enter a row to play(1-3): "))
    col = int(input("Enter a column to play(1-3): "))
    return (row-1, col-1)# then return that row and column instead of (0,0)
              
def hasBlanks(board):
    for row in board: # for each row in the board...
        for col in row: # for each square in the row...
           if col == 0: # check whether the square is blank
                return True # if so, return True

def main():
    board = [[0,0,0], [0,0,0], [0,0,0]]# TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1 # switch player for next turn
    printBoard(board)
main()
