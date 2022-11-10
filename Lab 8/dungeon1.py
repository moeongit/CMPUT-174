MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    grid = []
    with open(map_file, 'r') as file: 
        for line in file:
            convert = list(line.strip()) # Converts to a list and strips the "\n"
            grid.append(convert) # Appends the lists to the list grid
    print(grid)

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    


def get_command() -> str:
    """
    Gets a command from the user.
    """
    while True:
        user_input = input("> ")
        if user_input.lower() == "escape":
            exit()
        print("I do not understand.")


def main():
    """
    Main entry point for the game.
    """
    
    grid = load_map('cave_map.txt')
    # find_start(grid)
    get_command()
if __name__ == '__main__':
    main()