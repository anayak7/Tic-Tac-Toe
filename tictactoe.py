import random

board = [""] * 10


def draw_board():

    print('|_' + board[1] + '_|' + '|_' + board[2] + '_|' + '|_' + board[3] + '_|')
    print
    ""
    print('|_' + board[4] + '_|' + '|_' + board[5] + '_|' + '|_' + board[6] + '_|')
    print
    ""
    print('|_' + board[7] + '_|' + '|_' + board[8] + '_|' + '|_' + board[9] + '_|')


def player_input():
    #Takes player input for markers

    input1 = input("Enter your preferred marker, either X or O: ")
    input1 = input1.upper()

    if input1 == "X" or input1 == "O":
        return input1
    else:
        while input1 != "X" or input1 != "O":
            input1 = input("Please re-enter your preferred marker: ")
            input1 = input1.upper()

            if input1 == "X" or input1 == "O":
                return input


def place_marker(board, marker, position):
    #Places marker on tic-tac-toe board

    board[int(position)] = marker


def check_win(board, mark):
    #Checks for a wins

    winner = False
    if board[1] == board[2] == board[3] == mark:
        winner = True
    elif board[4] == board[5] == board[6] == mark:
        winner = True
    elif board[7] == board[8] == board[9] == mark:
        winner = True
    elif board[1] == board[5] == board[9] == mark:
        winner = True
    elif board[3] == board[5] == board[7] == mark:
        winner = True
    elif board[1] == board[4] == board[7] == mark:
        winner = True
    elif board[2] == board[5] == board[8] == mark:
        winner = True
    elif board[3] == board[6] == board[9] == mark:
        winner = True
    else:
        winner = False

    return winner


def choose_first():
    #Chooses which player goes first

    return random.randint(1, 2)


def space_check(board, position):
    #Checks if position already has a marker or not

    position1 = int(position)

    if board[position1] == "X" or board[position1] == "O":
        return True
    else:
        return False


def  full_board(board):
    #Checks for full board


    isFull = None

    for x in range(1, 9):
        if space_check(board, x) == True:
            continue
        else:
            return False

    return True


def replay():
    #Resets board for another game

    board = [""] * 10
    play_game()


def play_game():
    #Method that calls other methods

    print('Welcome to Tic-Tac-Toe!')

    num = choose_first()
    num2 = None
    if num == 1:
        num2 = 2
    else:
        num2 = 1
    marker = ""
    marker2 = ""
    if num == 1:
        print("Player 1 goes first")
        marker = player_input()
    else:
        print("Player 2 goes first")
        marker2 = player_input()

    if num == 1:
        if marker == 'X':
            marker2 = 'O'
        else:
            marker2 = 'X'
    else:
        if marker2 == 'X':
            marker = 'O'
        else:
            marker = 'X'

    print("Player1's marker is: ", marker)
    print("Player2's marker is: ", marker2)

    full = False
    while full == False:

        print("Player " + str(num) + " turn")

        position = input("Enter your position, it must be between (1,9)")
        space = space_check(board, position)
        if space == False:
            if num == 1:
                place_marker(board, marker, position)
            else:
                place_marker(board, marker2, position)
        else:
            while space:
                position1 = input("Enter another position.")
                space = space_check(board, position1)
            if space == False:
                if num == 1:
                    place_marker(board, marker, position)
            else:
                place_marker(board, marker2, position)

        draw_board()

        full = full_board(board)  # to check if the board is full
        if full == True:
            break
        else:
            win1 = check_win(board, marker)
            if num == 1:
                if win1 == True:
                    print("Player 1 is the winner.")
                    break
            else:
                win2 = check_win(board, marker2)
                if win2 == True:
                    print("Player 2 is the winner.")
                    break

        print("Player " + str(num2) + " turn")

        position = input("Enter your position, it must be between (1,9)")
        space = space_check(board, position)
        if space == False:
            if num == 1:
                place_marker(board, marker2, position)
            else:
                place_marker(board, marker, position)

        else:
            space1 = True
            while space1:
                position1 = input("Enter another position.")
                space1 = space_check(board, position1)
            if space1 == False:
                if num == 1:
                    place_marker(board, marker2, position)
                else:
                    place_marker(board, marker, position)

        draw_board()

        full = full_board(board)
        if full == True:
            break
        else:
            if num == 2:
                win2 = check_win(board, marker2)
                if win2 == True:
                    print("Player 2 is the winner.")
                    break
            else:
                win1 = check_win(board, marker)
                if win1 == True:
                    print("Player 1 is the winner.")
                    break

    if full == True:  # deciding the winner
        win1 = check_win(board, marker)
        win2 = check_win(board, marker2)

        if win1 == True and win2 == False:
            print("Player 1 is the winner.")
        elif win1 == False and win2 == True:
            print("Player 2 is the winner.")
        else:
           print("It's a tie!")

    answer = input("Do you want to play again? (Y/N)")
    answer = answer.capitalize()

    if answer == "Y":
        replay()
    else:
        exit


play_game()
