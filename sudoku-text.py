import random


class Cell:
    def __init__(self, value=None):
        self.value = value
        self.potentials = []
        self.do_not_add = []


class Sudoku:
    def __init__(self, grid):
        self.grid_simple = grid
        self.grid = [[Cell(grid[j][i]) for i in range(9)] for j in range(9)]

        self.update_potentials()

        print(self.grid[3][1].potentials)

    def update_potentials(self):
        for j in range(9):
            for i in range(9):
                if self.grid_simple[j][i] == 0:
                    self.grid[j][i].potentials = self.get_numbers(i, j)

    def get_numbers(self, x, y):
        potentials = []
        for pot in range(1, 10, 1):
            # Testing each number 1 to 9
            valid = True
            for value in self.grid_simple[y]:
                if value == pot:
                    valid = False
                    break

            if valid:
                for j in range(9):
                    if self.grid_simple[j][x] == pot:
                        valid = False
                        break

            if valid:
                quadrant = [x // 3, y // 3]
                for j in range(quadrant[1] * 3, quadrant[1] * 3 + 3, 1):
                    for i in range(quadrant[0] * 3, quadrant[0] * 3 + 3, 1):
                        if self.grid_simple[j][i] == pot:
                            valid = False
                            break

            if pot in self.grid[y][x].do_not_add:
                valid = False

            if valid:
                potentials.append(pot)

        return potentials

    def get_next(self, x, y):
        next_x = x + 1
        if next_x > 8:
            next_y = y + 1
            next_x %= 9
        else:
            next_y = y

        return next_x, next_y

    def solve(self, x, y):
        print(x, y)
        for j in range(9):
            print("         ", self.grid_simple[j])

        self.update_potentials()
        if self.grid[y][x].value == 0:
            guess_again = True
            while guess_again:
                if self.grid[y][x].potentials:
                    # Need to get a number for the grid
                    choice = self.grid[y][x].potentials.pop()
                    self.grid[y][x].value = choice
                    self.grid_simple[y][x] = choice

                    self.update_potentials()
                    next_x, next_y = self.get_next(x, y)

                    if next_y == 9:
                        print(next_x, next_y)
                        return False
                    else:
                        guess_again = self.solve(next_x, next_y)

                    self.grid[y][x].do_not_add.append(choice)
                    self.update_potentials()

                else:
                    return True
        else:
            next_x, next_y = self.get_next(x, y)

            if next_y == 9:
                print(next_x, next_y)
                return False
            else:
                return self.solve(next_x, next_y)


def main():
    puzzle = Sudoku(test1)
    puzzle.solve(0, 0)
    for j in range(9):
        print(puzzle.grid_simple[j])


test1 = [[0, 0, 7, 9, 3, 0, 2, 5, 4],
         [9, 0, 0, 0, 0, 0, 8, 0, 0],
         [4, 0, 6, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 8, 1, 5, 6, 0],
         [0, 6, 0, 5, 0, 3, 0, 2, 0],
         [0, 5, 8, 4, 6, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 6, 0, 9],
         [0, 0, 2, 0, 0, 0, 0, 0, 5],
         [8, 9, 4, 0, 1, 5, 7, 0, 0]]

main()
