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

def main() -> None:
    grid = create_grid("data_1.txt")
    print("Sim City Land Values:")
    display_grid(grid)
main()