"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jaroslav Brodacky
email: jbrodacky@gmail.com
"""

separator = "=" * 65

gameboard_lst = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # gameboard positions (empty, O or X)

game_end = False
check_entry = False
board_separator = "+---+---+---+"
win_combination = [      # definition of winning combinations i.e. positions of the same char on the board
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


def draw_board():  
    """Function to redraw the whole board with current values."""
    print(separator)
    print(board_separator)
    for x in range(1, 10, 3):
        print(
            "|",
            gameboard_lst[x - 1],
            "|",
            gameboard_lst[x],
            "|",
            gameboard_lst[x + 1],
            "|",
        )
        print(board_separator)
    print(separator)


def check_input(inp: str) -> bool:  
    """ Function to check if the input is a number 1-9. Output: boolean. """

    if not inp.isdigit(): # checking if number is a digit
        print(separator)
        print("Not a number. Selection needs to be a number in the range 1 to 9.")
        return False
    
    elif int(inp) in range(1, 10) and gameboard_lst[int(inp) - 1] == " ": # checking if number is in the range 1-9
        return True
    
    elif int(inp) in range(1, 10) and gameboard_lst[int(inp) - 1] != " ": # checking if chosen position is occupied
        print(separator)
        print("Gameboard position is already occupied, please choose another.")
        return False
    
    else:
        print(separator)
        print("Selection needs to be a number in the range 1 to 9.")
        return False


def check_end (gameboardvalue_lst: list,) -> bool: 

    """ Function to check if game ended in victory or in a draw.
        Output: boolean. Win, draw: True """

    checked_list = []

    for (checked_list) in (win_combination):  
        # checking if there is any winning combination of 3 non empty chars in line_row_diagonal

        if ( 
            gameboardvalue_lst[checked_list[0] - 1]
            == gameboardvalue_lst[checked_list[1] - 1]
            == gameboardvalue_lst[checked_list[2] - 1]
        ) and gameboardvalue_lst[checked_list[0] - 1] != " ": 
            print(f"Congratulations, the player {gameboardvalue_lst[checked_list[0] - 1]} WON!")
            print(f"Winning combination were positions: {checked_list}.")
            return True

    if (" " not in gameboardvalue_lst):     # check if game ends because of no empty playing fields 
        print("Game ended in draw, no empty playing fields remain.")
        return True

    return False


#game start

print(
    """Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game"""
)


draw_board()

while not game_end:

    hrac_O = input("Player O | Please enter your move number:")  # hrac_0 move

    while not check_input(hrac_O): # check if the input value is a number 0-9
        draw_board()
        hrac_O = input("Player O | Please enter your move number:")

    gameboard_lst[int(hrac_O) - 1] = "O" # enter the chosen value to the gameboard
    draw_board() #redraw board with the new character
    game_end = check_end(gameboard_lst) #check if game was ended (won_drawn)

    if game_end:
        break


    hrac_1 = input("Player X | Please enter your move number:") # hrac_1 move

    while not check_input(hrac_1): # check if the input value is a number 0-9
        draw_board() 
        hrac_1 = input("Player X | Please enter your move number:")

    gameboard_lst[int(hrac_1) - 1] = "X" # enter the chosen value to the gameboard
    draw_board() #redraw board with the new character
    game_end = check_end(gameboard_lst) #check if game was ended (won_drawn)
