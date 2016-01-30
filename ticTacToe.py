def printBoard(board):
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
    print(board['top-L']+'|'+ board['top-M']+ '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or 
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
    (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or 
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or 
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or 
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or 
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))  
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #sets up the first turn
    for i in range(9): #determines if the turn is 1-9
        printBoard(board) #runs printBoard function
        print('Turn for ' + turn + '. Move on which space?') #prints asking the player where to move
        move = input()#interprets the players move
        board[move] = turn#puts the move on the board
        if( checkWinner(board, 'X') ):#checks to see if the X player won
            print('X wins!')#prints if X wins
            break#ends the game after X wins
        elif ( checkWinner(board, 'O') ):#checks to see if O player won
            print('O wins!')#prints if O wins
            break#ends the game after O wins
    
        if turn == 'X':#After X goes
            turn = 'O'#it's O's Turn
        else:
            turn = 'X'#if it's not O's turn, then it's X's turn
        
    printBoard(board)#runs printBoard function
    
