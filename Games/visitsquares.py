# Visit All Squares


import random


GAME_PIECE = "@"
MAX_VISITS = 3


def create_board(size: int)-> list:
    # Creates a board with the given size
    board = [0] * size
    return board # Throw



def display_board(board, current_position):
    display_str = "|"
    for index in range(len(board)):
        if index == current_position:
            display_str = f'{display_str}{GAME_PIECE}{board[index]}|'
        else:
            display_str = f'{display_str}{board[index]}|'
        print("=" * len(display_str))
        print(display_str)
        print("=" * len(display_str))



def roll_die(sides: int)-> int:
    # Returns a number between 1 and number of sides
    input("Press enter to roll. ")
    number = random.randint(1, sides)
    return number # Throw



def update_board(board, current_position, value):
    # Updates the board
    new_position = (current_position + value) % len(board)
    board[new_position]= board[new_position] + 1
    return new_position # Throw

def is_game_over(board):

    return MAX_VISITS in board or 0 not in board


def main():
    game_over = False
    current_position = -1
    board_size = int(input("What is the board size? "))
    board = create_board(board_size) # Catch
    display_board(board, current_position)
    size = int(input("How many sides does your die have? "))
    while not game_over:
        value = roll_die(size) # Catch
        print(f"You have rolled a {value}")
        current_position = update_board(board, current_position, value) # Catch
        display_board(board, current_position)
        game_over = is_game_over(board)
main()