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

def main():
    grid = load_map('cave_map.txt')
    print(grid)
    starting_position = find_start(grid)
    print(f"Starting position: {starting_position}")
    get_command()

if __name__ == '__main__':
    main()