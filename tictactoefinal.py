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


# Defines options available for making a move on the board
def availablePlace(board, movesList):
    options = []
    for i in movesList:
        if FreePlace(board, i):
            options.append(i)
    if len(options) != 0:
        return random.choice(options)
    else:
        return None


# Defines computer as opposite letter from Player
def Computer(board, computer):
    if computer == 'X':
        player = 'O'
    else:
        player = 'X'

# Checks if computer can win
    for i in range(1, 10):
        copy = newBoard(board)
        if FreePlace(copy, i):
            makeMove(copy, computer, i)
            if Winner(copy, computer):
                return i


# Check if player can win
    for i in range(1, 10):
        copy = newBoard(board)
        if FreePlace(copy, i):
            makeMove(copy, player, i)
            if Winner(copy, player):
                return i

# Moves to numbers [1, 3, 7, 9] if free
    move = availablePlace(board, [1, 3, 7, 9])
    if move != None:
        return move

# Moves to number 5 if free
    if FreePlace(board, 5):
        return 5

# Moves to numbers [2, 4, 6, 8] if free
    return availablePlace(board, [2, 4, 6, 8])

# Checks are there any free places left on the board
def noFreePlace(board):
    for i in range(1, 10):
        if FreePlace(board, i):
            return False
    return True

# Asks player does he/she want to play another game
def AnotherGame():
    print('Do you want another game? (yes or no)')
    return input().lower().startswith('y')

print('Welcome to Tic Tac Toe!')

# Chooses who goes first bassed on Player1 letter and if Player1 won or it is draw
while True:
    theBoard = [' '] * 10
    player, computer = chooseLetter()
    turn = FirstMove()
    print('The ' + turn + ' goes first.')
    game_on = True
    while game_on:
        if turn == 'player':
            drawBoard(theBoard)
            move = Player1(theBoard)
            makeMove(theBoard, player, move)
            if Winner(theBoard, player):
                drawBoard(theBoard)
                print('Yaaay! You won!')
                game_on = False
            else:
                if noFreePlace(theBoard):
                    drawBoard(theBoard)
                    print('It is a draw!')
                    break
                else:
                    turn = 'computer'

# Computer chooses moves and checks if Computer won or it is draw
        else:
            move = Computer(theBoard, computer)
            makeMove(theBoard, computer, move)
            if Winner(theBoard, computer):
                drawBoard(theBoard)
                print('Sorry, you lost!')
                game_on = False
            else:
                if noFreePlace(theBoard):
                    drawBoard(theBoard)
                    print('It is a draw!')
                    break
                else:
                    turn = 'player'

# Asks do we want to play again if not exits game
    if not AnotherGame():
        print('Thanks for playing!')
        break
