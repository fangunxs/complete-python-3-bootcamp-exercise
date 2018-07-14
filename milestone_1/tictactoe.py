'''
found 2 bugs:
[2,3,4] is not a winning moves but, it has distance 1
[3,5,7] is a winning moves, but it has distance 2
[1,3,5,7] is a winning moves, but our logic consider this winning is wrong
'''
import random

def main():
    # Welcome message
    print('Welcome to Tic Tac Toe!')

    if isPlayerReady():
        # have players' markers
        playerMarkers = playerInput()
        # init the data for game board and the moves of players
        board = [' '] * 10
        playerMoves = [[], []]
        player = None
        # game logic
        while shouldGameContinue_update(player, playerMarkers, board):
            player = getNextPlayer(player)
            #playerMoves[player] = placeMarker(playerMarkers[player], playerMoves[player])
            nextMove = placeMarker(board)
            playerMoves[player].append(nextMove)
            board[nextMove] = playerMarkers[player]
            drawGameBoard(board)
        else:
            main()

def isMoveValid(move, board):
    return board[move] == ' '

def getNextPlayer(player):
    playerOptions = (1,2)
    if player is None:
        # generate a random number, by simulating flipping a coin, to decide playing order
        player = random.randint(0,1)
        print('Player {} will go first.'.format(playerOptions[player]))
    else:
        player += 1
        player %= 2
        # Alert player to place marker
        print('Next is Player{}'.format(playerOptions[player]))
    return player

def placeMarker(board):
    position = input('Choose your position: (1-9)')
    try:
        position = int(position)
    except ValueError:
        print('Please enter an integer from 1 to 9.')
        return placeMarker(board)

    if isUserInputValid(position, list(range(1, 10))):
        if isMoveValid(position, board):
            return position
        else:
            print('This position has been taken.')
            return placeMarker(board)
    else:
        print('Please only input integer from 1 to 9.')
        return placeMarker(board)

def shouldGameContinue_update(player, markers, board):
    if player == None:
        return True
    else:
        #check winning conditions
        if (board[1] == board[2] == board[3] == markers[player] or
        board[4] == board[5] == board[6] == markers[player] or
        board[7] == board[8] == board[9] == markers[player] or
        board[1] == board[4] == board[7] == markers[player] or
        board[2] == board[5] == board[8] == markers[player] or
        board[3] == board[6] == board[9] == markers[player] or
        board[1] == board[5] == board[9] == markers[player] or
        board[3] == board[5] == board[7] == markers[player]):
            print('player{} won the game!!!'.format(player + 1))
            return False
        elif isBoardFull(board):
            #this is a tied game when the board is full and there is no winner
            print('The game is tied!')
            return False
        else:
            return True

def isBoardFull(board):
    #when there is no blank string in board array, the board is full
    return ' ' not in board[1:]

def shouldGameContinue(player, playerMoves):
    '''
    winning requirements for a player are:
        a. the distances betweens moves either 1, 3 or 4
        b. have same distances in the distance array
    example:
        a. winning mvoes:
            [1,2,3], distance array is [1,2,1]
            [1,4,7], distance array is [3,6,3]
            [1,5,9], distance array is [4,8,4]
        b: not winning moves:
            [1,3,5], distance array is [2,4,2]
    '''
    acceptableDistance = [1,3,4]
    if player == None:
        return True
    else:
        distances = getMovesDistance(playerMoves[player])
        if foundSameDistance(distances, acceptableDistance):
            print('player{} won the game!!!'.format(player + 1))
            return False
        else:
            return True

def isPlayerReady():
    # Start the game
    ready = input('Are you ready to play(y/n)?')
    if isUserInputValid(ready, ('y', 'n')):
        return ready == 'y'
    else:
        print('Please only input "y" or "n"')
        return isPlayerReady()

def isUserInputValid(*args):
    userInput = args[0]
    validRange = args[1]
    return userInput in validRange

def playerInput():
    '''
    Player1 and Player2 choose marker
    The return value is a tuple: (player one marker, player two marker)
    '''
    playerOneMarker = input('Play 1: Do you want to be X or O?')
    if isUserInputValid(playerOneMarker, ('X', 'O')):
        markers = ('X','O') if playerOneMarker == 'X' else ('O','X')
        return markers
    else:
        print('Please only input "X" or "O"')
        return playerInput()

def foundSameDistance(distances, acceptableDistance):
    '''
    check if there are multiple acceptable distance in distances array 
    '''
    #return len(set(distances)) < len(distances)
    for distance in acceptableDistance:
        if distances.count(distance) > 1:
            return True
    return False

def getMovesDistance(moves):
    '''
    return an array with distance of the moves
    example: moves are 1,3,5( moves equals to [1,3,5])
             distances are 2(abs value from 1 to 3), 4(abs value from 1 to 5),
             2(abs value from 3 to 5)
             distances equals to [2,4,2]
    '''
    distances = []
    for index, value in enumerate(moves):
        nextMove = index + 1
        while nextMove < len(moves):
            distances.append(abs(value - moves[nextMove]))
            nextMove += 1
    return distances

def drawGameBoard(gamePlayed):
    # 0 index position here is a non valid position, just for filling purpose
    gameBoard = '''{0}
     {1} | {2} | {3} 
    ---|---|---
     {4} | {5} | {6}
    ---|---|---
     {7} | {8} | {9} 
    '''.format('', gamePlayed[1], gamePlayed[2], gamePlayed[3], gamePlayed[4], 
    gamePlayed[5], gamePlayed[6], gamePlayed[7], gamePlayed[8], gamePlayed[9])
    print(gameBoard)

if __name__ == '__main__':  main()

#def startGame(player1, player2):
#    position_match = [' '] * 9
#
#    playerOneMoves = []
#    playerTwoMoves = []
#
#    while True:
#        playerOneNextMove = int(nextMove()) - 1
#        playerOneMoves.append(playerOneNextMove)
#        position_match[playerOneNextMove] = player1
#        drawGameBoard(position_match)
#        if isWon(player1, playerOneMoves):
#            break
#
#        playerTwoNextMove = int(nextMove()) - 1
#        playerTwoMoves.append(playerTwoNextMove)
#        position_match[playerTwoNextMove] = player2
#        drawGameBoard(position_match)
#        if isWon(player2, playerTwoMoves):
#            break
#
#    isPlayAgain = input('Do you want to play again(y/n)?')
#    if isPlayAgain == 'y':
#        main()