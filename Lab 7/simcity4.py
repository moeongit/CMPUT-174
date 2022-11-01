def create_grid(filename: str) -> list[list[int]]: # This function reads a file and creates a grid from the numbers in the file
    with open(filename, "r") as filename:
        str_nums = filename.readlines()
    int_nums = []
    for i in str_nums:
        int_nums.append(int(i))
    height = int_nums[0]
    width = int_nums[1]
    grid = []
    count = 2
    for i in range(height):
        rows = []
        for i in range(width):
            rows.append(int_nums[count])
            count += 1
        grid.append(rows)
    return grid

def display_grid(grid: list[list[int]]) -> None: # Displays the grid
    for i in grid:
        for nums in i:
            print(f"{nums:10}", end = "") # Aligns the numbers
        print()

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]: # This function finds the values of the neighbours
    """
    Find the neighbors of a cell
    """
    neighbours = [] # Created a list to append to later
    rows = len(grid[0]) # Rows is the first number in the txt
    cols = len(grid[1]) # Columns is the second number in the txt
    for i in range(row - 1, row + 2): # Had permission to use this code from class
        for j in range (col - 1, col + 2):
            if i == row and j == col:
                continue
            if i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            neighbours.append(grid[i][j])
    return neighbours
 
def fill_gaps(grid: list[list[int]]) -> list[list[int]]: # Fills the 0's, adds the numbers of the neighbors of 0 and divides them to get the average, fills that number in 0
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    for row in range(len(grid[0])):
        for col in range(len(grid[1])):
            if grid[row][col] == 0:
                average = 0
                close_neighbors = find_neighbor_values(grid, row, col)
                for i in close_neighbors:
                    average += i
                new_number = round(average/(len(close_neighbors)))
                grid[row][col] = new_number
    return grid

def find_max(grid: list[list[int]]) -> int: # Finds the max number from the grid
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    large_num = []
    for row in range(len(grid)):
        for col in grid[row]:
            large_num.append(col)
    return max(large_num)


def find_average(grid: list[list[int]]) -> int: # Finds the average number in the grid
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    large_num = 0
    for row in range(len(grid)):
        for col in grid[row]:
            large_num = large_num + col
    average = large_num/(len(grid) * len(grid[0]))

    return round(average)
    
def main() -> None: # Main function - calls all the functions
    """
    Main program.
    """
    grid = create_grid("data_2.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")
main()