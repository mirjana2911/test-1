# Tic Tac Toe

import random

# Draws empty board
def drawBoard(board):
    
    print("  "+board[7]+"| "+board[8]+" | "+board[9]+"  ")
    print("---|---|---")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
    print("---|---|---")
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")

# Makes player choose X or O and assigns computer opposite value from the player
def chooseLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

# Defines who will make first move, if player chooses X computer will go first, if player chooses O he will go first
def FirstMove():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter

# Defines options for winning the game
def Winner(Player1, Computer):
    return ((Player1[7] == Computer and Player1[8] == Computer and Player1[9] == Computer) or 
    (Player1[4] == Computer and Player1[5] == Computer and Player1[6] == Computer) or 
    (Player1[1] == Computer and Player1[2] == Computer and Player1[3] == Computer) or 
    (Player1[7] == Computer and Player1[4] == Computer and Player1[1] == Computer) or 
    (Player1[8] == Computer and Player1[5] == Computer and Player1[2] == Computer) or 
    (Player1[9] == Computer and Player1[6] == Computer and Player1[3] == Computer) or 
    (Player1[7] == Computer and Player1[5] == Computer and Player1[3] == Computer) or 
    (Player1[9] == Computer and Player1[5] == Computer and Player1[1] == Computer)) 

def newBoard(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

# Defines can a player move to that position or is the position taken
def FreePlace(board, move):
    return board[move] == ' '

# Defines where player wants to move on the board
def Player1(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not FreePlace(board, int(move)):
        print('Please choose position 1-9!)')
        move = input()
    return int(move)

