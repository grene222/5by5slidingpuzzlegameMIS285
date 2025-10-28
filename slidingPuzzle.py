import random, sys

BLANK = '  '

#this is our main game loop
#it calls our function that randomly scrambles the board
#it then stores our random board in the variable gameBoard
#it is an infinite loop until the player wins, quits, or uses the help
#it displays our formatted game puzzle
#it asks for the next player move
#it handles the auot solve command
#if player types help, it will start the auto solver
#it also checks if the player has won the game or not
# ultimatly, its a constant loop that shows the board, waits for a user input, updates the board, and checks if the board is solved.
def main():
    print('Sliding Tile Puzzle, by Kevin and Brian')
    print('Use the W,A,S, and D keys to move the tiles back into their original order:')
    input('Press Enter to begin the puzzle!')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)

        if playerMove == 'HELP':
            print("Solving!")
            steps = helpSolve(gameBoard)
            displayBoard(gameBoard)
            if isSolved(gameBoard):
                print(f'Solved in {steps} moves.')
                sys.exit()
            continue

        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()

#this defines if the board is complete or not
#if the board is not in a complete state, it returns false
def isSolved(board):
    return board == getNewBoard()

#this is our attempt at an auto-solver
#it makes 1000 legal moves and shows the process every 50 moves
#it counts how many moves there have been
#the program keeps going until it has been solved with random moves or if it hit 1000 moves
def helpSolve(board, max_moves = 1000, show_move = 50):
    steps = 0
    last = None
    while not isSolved(board) and steps < max_moves:
        last = makeRandomMove(board, last_move=last)
        steps += 1
        if steps % show_move == 0:
            print(f"[auto] steps = {steps}")
            displayBoard(board)
        
    if isSolved(board):
        return steps
    return None

#this function build a list that represents what the solved puzzle looks like
def getNewBoard():
    return [['1 ', '6 ', '11', '16', '21'],
            ['2 ', '7 ', '12', '17', '22'],
            ['3 ', '8 ', '13', '18', '23'],
            ['4 ', '9 ', '14', '19', '24'],
            ['5 ', '10', '15', '20', BLANK]]

#this part is what makes the game look like the game
#it takes the list and formats it into a way to see the game correctly
def displayBoard(board):
    labels = [board[0][0], board[1][0], board[2][0], board[3][0], board[4][0],
            board[0][1], board[1][1], board[2][1], board[3][1], board[4][1],
            board[0][2], board[1][2], board[2][2], board[3][2], board[4][2],
            board[0][3], board[1][3], board[2][3], board[3][3], board[4][3],
            board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]]
    boardToDraw = """
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
""".format(*labels)
    print(boardToDraw)

#this function is what finds the blank space in the game
#the x represents the rows and the y represents the collums
#when it finds the blank space, it returns the cordinates of the space.
def findBlankSpace(board):
    for x in range(5):
        for y in range(5):
            if board[x][y] == BLANK:
                return (x, y)

#this part accepts the player movement or input by the player
#it starts by finding the blank tile
#then it finds if a move will be legal or not
#it starts a loop of asking the player which option it will choose
#it takes the player input
#if move is not legal, the loop repeats.
def askForPlayerMove(board):
    blankx, blanky = findBlankSpace(board)
    w = 'W' if blanky != 4 else ' '
    a = 'A' if blankx != 4 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print('                          ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))
        print('Type HELP for auto solve!')

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response == 'HELP':
            return 'HELP'
        if response in (w + a + s + d).replace(' ', ''):
            return response
        
#this is the atcual movement of the tiles
#it finds the position of the blankspace
#it takes player input so if they use the WASD keys, it moves the tiles respectivly
def makeMove(board, move):
    bx, by = findBlankSpace(board)

    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]

#this defines what a legal move is for the program.
#it tells the program that if the blank space is near a wall it can only move the other way.
#it uses the random import to make a random legal move
def makeRandomMove(board, last_move = None):
    blankx, blanky = findBlankSpace(board)
    validMoves = []

    if blanky != 4:validMoves.append('W')
    if blankx != 4:validMoves.append('A')
    if blanky != 0:validMoves.append('S')
    if blankx != 0:validMoves.append('D')

    makeMove(board, random.choice(validMoves))

#this part of the program is what creates the random board at the start of the game
#at the start of the program, it runs 200 random moves which suffles the board, kind of like a rubix cube.
def getNewPuzzle(moves=200):
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board

# this part of the code means that the program will run only if it is the main script.
# this means if someone else imports this program, it will not run unless the told to do so
if __name__ == '__main__':
    main()