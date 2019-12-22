# Given a text file that has sudoku grids written as 81 digits, it will format them in the grid type.
# Then copy over the output into the sudoku-text.py file.

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

print(grids)
