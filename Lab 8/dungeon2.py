import copy

MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    grid = []
    with open(map_file, 'r') as file: 
        for line in file:
            convert = list(line.strip()) # Converts to a list and strips the "\n"
            grid.append(convert) # Appends the lists to the list grid
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    starting_letter = "S"
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == starting_letter:
                starting_index = [i, j]
                break
    return starting_index

def get_command() -> str:
    while True:
        user_input = input("> ")
        if user_input.lower() == "escape":
            exit()
        print("I do not understand.")

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    user_input = input("> ")
    new_grid = copy.deepcopy(grid)
    row = player_position[0]
    col = player_position[1]
    new_grid[row][col] = "@"
    if user_input.lower() == "show map":
        for i in new_grid:
            for j in i:
                print(j, end = "")
            print()

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    return [rows, cols]
    
def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    if (position[0] > grid_rows) and (position[1] > grid_cols):
        return False
    elif (position[0] < grid_rows) and (position[1] > grid_cols):
        return False
    elif (position[0] > grid_rows) and (position[1] < grid_cols):
        return False
    elif (position[0] < grid_rows) and (position[1] < grid_cols):
        return True
    elif (position[0] == grid_rows) and (position[1] == grid_cols):
        return True

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    # TODO: implement the rest of the function

def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    starting_position = find_start(grid)
    display_map(grid, starting_position)
    get_grid_size(grid)
    print(is_inside_grid(grid, (4, 5)))

    
if __name__ == '__main__':
    main()
