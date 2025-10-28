import random, sys

BLANK = '  '

def main():
    print('Sliding Tile Puzzle, by Kevin and Brian')
    print('Use the WASD keys to move the tiles back into their original order:')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()


def getNewBoard():
    return [['1 ', '6 ', '11', '16', '21'],
            ['2 ', '7 ', '12', '17', '22'],
            ['3 ', '8 ', '13', '18', '23'],
            ['4 ', '9 ', '14', '19', '24'],
            ['5 ', '10', '15', '20', BLANK]]

#added 1 more row and collum to this function.
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

### changed the x and y range to 5 instead of 4 to accomadate the new grid
def findBlankSpace(board):
    for x in range(5):
        for y in range(5):
            if board[x][y] == '  ':
                return (x, y)

def askForPlayerMove(board):
    blankx, blanky = findBlankSpace(board)
    w = 'W' if blanky != 4 else ' '
    a = 'A' if blankx != 4 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print('                          ({})'.format(w))
        print('Enter WASD (or QUIT): ({}) ({}) ({})'.format(a, s, d))

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response

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

def makeRandomMove(board):
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 4:
        validMoves.append('W')
    if blankx != 4:
        validMoves.append('A')
    if blanky != 0:
        validMoves.append('S')
    if blankx != 0:
        validMoves.append('D')

    makeMove(board, random.choice(validMoves))

def getNewPuzzle(moves=200):
    board = getNewBoard()

    for i in range(moves):
        makeRandomMove(board)
    return board

if __name__ == '__main__':
    main()
