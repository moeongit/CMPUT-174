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
    starting_index = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == starting_letter: # Append to the list starting_index 
                starting_index.append(i)
                starting_index.append(j)
                break # Breaks the loop
    return starting_index # Gives us the starting position

def get_command() -> str:
    while True:
        user_input = input("> ")
        if user_input.lower() == "escape": # If the user types escape, the function will exit
            exit()
        print("I do not understand.") # Else, it will print "I do not understand."

def main():
    grid = load_map('cave_map.txt')
    print(grid)
    starting_position = find_start(grid)
    print(f"Starting position: {starting_position}")
    get_command()

if __name__ == '__main__':
    main()