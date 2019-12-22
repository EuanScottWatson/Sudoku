file = open("sudoku_grids", "r")
contents = file.read()

grids = []
current_grid = [[] for _ in range(9)]
y = 0

for value in contents:
    if value == '\n':
        grids.append(current_grid)
        current_grid = [[] for _ in range(9)]
    else:
        current_grid[y].append(int(value))

    if len(current_grid[y]) == 9:
        y = (y + 1) % 9

for grid in grids:
    for j in range(9):
        print(grid[j])
    print("")

print(grids)
