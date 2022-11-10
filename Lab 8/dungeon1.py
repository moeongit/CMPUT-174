MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    grid = []
    with open(map_file, 'r') as file:
        for line in file:
            convert = list(line.strip())
            grid.append(convert)
    print(grid)

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    # TODO: implement this function

def get_command() -> str:
    """
    Gets a command from the user.
    """
    # TODO: implement this function


def main():
    """
    Main entry point for the game.
    """
    load_map('cave_map.txt')
if __name__ == '__main__':
    main()