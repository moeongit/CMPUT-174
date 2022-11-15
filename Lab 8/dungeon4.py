
MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    # Implemented in version 1

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    # Implemented in version 1

def get_command() -> str:
    """
    Gets a command from the user.
    """
    # Implemented in version 1

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    # TODO: update this function

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    # Implemented in version 2

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    # Implemented in version 2

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    # Implemented in version 2

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    # Implemented in version 3

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    # TODO: implement this function

def display_help() -> None:
    """
    Displays a list of commands.
    """
    # TODO: implement this function

def main():
    """
    Main entry point for the game.
    """
    # TODO: update the main() function

if __name__ == '__main__':
    main()

