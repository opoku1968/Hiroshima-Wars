from random import randint

player = []
player_guesses = []
compuer = []


def make_board(board):
    """
    Make the starting board of 5 "X" in 5 lists
    Arguments: an empty list
    Returns: a list containing 5 lists of the letter X
    """
    for i in range(5):
        board.append([" X "]*5)
    return doard


def print_board(board):
    """
   Display the board elements marked with 'X', presenting them 
   in a format without the original list structure 
   and with added spaces.
    """
    for ind in board:
        print(" ".join(ind))


def random_num(board):
    """
    Generate a random number between 0 and one less than the length 
    of the board. This adjustment is made because the indices
      in the board's list start at 0, while the len function begins counting at 1.
    """
    return randint(0, len(board)-1)



def generate_ship_loc(board):
    """
    We want 4 ships to be on the board and the while loop ensures there will
    be. It generates random co-ordinates, places the "o", then counts how many
    "o" are in the board's lists, keeping track with variable ship_num. If that
    number is less than 4, it loops again. This should catch if any locations
    are randomly generated more than once.
    Argument: a list, expected to be the populated players board
    """
    ship_num = 0
    while ship_num < 4:  # we want 4 ships to be on the board
        ship_num = 0  # reset ship_num value every loop
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_row][ship_col] = " o "
        # for every list in the board, we look for " o " and keep a running
        # total with ship_num
        for row in board:
            ship_num += row.count(" o ")



def welcome():
    """
    Opening message to the game that also takes in a username.
    """
    print("Welcome to you vs. computer")
    username = input("Type in a username and press return: \n")
    print(f'\nHi {username}! We will auto generate your battleship locations.'
          'You have 4 battleships to find within the computer\'s board.')
    print('\nX are empty locations, * are shots that missed and # are hits'
          'Be aware that the grid is five wide using integers between 1 and 5')


def generate_boards():
    """
    Prepare all the necessary game boards: one for the player's battleships, one for 
    the computer's hidden battleships, and one for the player's guesses. The player's board 
    will hold their ships, while the computer will attempt to locate them. The computer's 
    board will contain its ships, hidden from the player, and the player_guesses board will display 
    the computer's board but without revealing the location of the computer's ships to the player.
    """
    make_board(player)
    make_board(computer)
    make_board(player_guesses)
    generate_ship_loc(player)
    generate_ship_loc(computer)


def player_guess():
    """
    Get player input on battleship guess, check whether it is valid data,
    check whether that shot has already been taken, check whether they hit a
    battleship and show them the result of their turn.
    """
    print("Here is the computer's board:")
    print_board(player_guesses)
    repeat = True
    while repeat:
        # check whether data is valid
        while True:
            print("\nWhich column would you like to fire at?")
            guess_col = input("Enter a number and press enter: \n")
            if validate_data(guess_col):
                break
        while True:
            print("\nWhich row would you like to fire at?")
            guess_row = input("Enter a number and press enter: \n")
            if validate_data(guess_row):
                break

        # minus 1 as the players enter numbers between 1 and 5
        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1

        # check if we've already chosen that spot
        if (player_guesses[guess_row][guess_col] == " * " or
                player_guesses[guess_row][guess_col] == " # "):
            print("You've already picked that spot, try again!")
        else:
            repeat = False
    # Check whether that spot is a hit or not and display result
    if computer[guess_row][guess_col] == " o ":
        player_guesses[guess_row][guess_col] = " # "
        print("\nYAY! You hit their ship!")
    else:
        player_guesses[guess_row][guess_col] = " * "
        print("\nOh no! You missed their ship :(")


def computer_guess():
    """
    Computer guess at player board using randomly generate co-ordinates
    """
    print("\n\nNow the computer's turn!")
    repeat = True
    # Generate first random numbers
    guess_col = randm_num(computer)
    guess_row = random_num(computer)
    # Check if we've already chosen that spot
    while repeat:
        if (player[guess_row][guess_col] == " * " or
                player[guess_row][guess_col] == " # "):
            guess_col = random_num(computer)
            guess_row = random_num(computer)
        else:
            repeat = False
    # Display to the player what the computer chose and result
    print(f"They've chosen {guess_col + 1}, {guess_row + 1}")
    if player[guess_row][guess_col] == " o ":
        player[guess_row][guess_col] = " # "
        print("It's a hit! :(")
    else:
        player[guess_row][guess_col] = " * "
        print("YAY! They missed!")


def game_play():
    """
    Main loop for playing the game. First generate the boards and display the
    welcome message. Then, there's a while loop so that we can take a maximum
    of then turns. In the while loop, we display with turn it is, then run the
    player guess, print and computer guess functions. Then each turn, we check
    whether there is a winner, if there is, we exit the loop and run the final
    winning check and message function. If after all the turns, there is no
    winner, we still run the final winning check function.
    """
    generate_boards()
    welcome()
    i = 0
    while i < 10:
        print(f"\nThis is turn {i +1}/10 \n")
        player_guess()
        print_board(player_guesses)
        input("\nPress Enter to continue...")
        computer_guess()
        print("\nHere's your board: ")
        print_board(player)
        input("\nPress Enter to continue...")
        i += 1
        if check_winner(player) == 4:
            i = 10
        elif check_winner(player_guesses) == 4:
            i = 10
    check_winner_final()


def validate_data(value):
    """
    If values is not between 1 and 5, raise an error and request a new input
    Argument: player input value
    """
    try:
        if int(value) > 5 or int(value) < 1:
            raise ValueError(
                "Your shot is out of bounds! Choose a number between 1 and 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        print("Please enter an integer between 1 and 5")
        return False
    return True


def check_winner(board):
    """
    Sums the number of times " # " (hit battleships) appear in the board.
    Argument: a list, expected to be the player board
    """
    total = 0
    for list in board:
        total += list.count(" # ")
    return total

def check_winner_final():
    """
    Check for a winner after ten turns and report the result to the player
    """
    player_result = check_winner(player_guesses)
    computer_result = check_winner(player)
    if player_result > computer_result:
        print("Congratulations! You WIN!")
    elif player_result < computer_result:
        print("Commiserations - the computer had the most hits!")
    else:
        print("It was a draw!")


# Call the main function
game_play()

