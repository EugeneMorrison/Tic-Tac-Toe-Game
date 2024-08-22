import random

#set global variables: board, currentPlayer, winner, game Running
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"] #A list representing a game board consisting of 9 elements (3x3). Each element contains a "-" character to indicate an empty cell.

currentPlayer = "X" #human player
winner = None #Variable to store the winner. Initially None.
gameRunning = True #Flag to control the main game loop. Initially True

# game board
def printBoard(board): #The function displays the current state of the game board in a convenient format
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
# this functon ask the user to select a number one through nine
# and each number is going to correspond with a section on the game board.
# Thus inp returns integer on the place of empty section.
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": #set that the input is a valid number one through nine and the board that the player inputted is empty (has a dash) so no player has gone there yet
        board[inp-1] = currentPlayer # If the cell is empty (has a dash), the current player's symbol ( in our case "X") is written there
    else:
        print("Oops player is already at that spot.")


# check for win or tie

# Function for checking horizontal lines.
# If all three elements in one of the lines are equal and not equal to "-", then there is a winner.
# The function sets winner to the value of this line and returns True.
def checkHorizontle(board):
    global winner # we tap into one of the global variables we made earlier which is that winner variable
    # So if we make changes to the winner variable within the scope of this function, the winner variable changes within the scope of the entire file
    # if check horizontal is True then we can break out the game loop
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfTie(board)
    checkIfWin(board)
    switchPlayer()
    computer(board)
    checkIfTie(board)
    checkIfWin(board)