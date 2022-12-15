from copy import deepcopy

def create_grid(filename: str) -> list[list[int]]:
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

def display_grid(grid: list[list[int]]) -> None:
    for i in grid:
        for nums in i:
            print(f"{nums:10}", end = "")
        print()

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    neighbours = []
    rows = len(grid[0])
    cols = len(grid[1])
    for i in range(row - 1, row + 2):
        for j in range (col - 1, col + 2):
            if i == row and j == col:
                continue
            if i < 0 or j < 0 or i >= rows or j >= cols:
                continue
            neighbours.append(grid[i][j])
    return neighbours
 
def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
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

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_1.txt")
    print("Sim City land values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
main()