class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def check_valid(self, x, y, pot):
        # Testing each number 1 to 9
        for value in self.grid[y]:
            if value == pot:
                return False

        for j in range(9):
            if self.grid[j][x] == pot:
                return False

        quadrant = [x // 3, y // 3]
        for j in range(quadrant[1] * 3, quadrant[1] * 3 + 3, 1):
            for i in range(quadrant[0] * 3, quadrant[0] * 3 + 3, 1):
                if self.grid[j][i] == pot:
                    return False

        return True

    def return_first_empty(self):
        for j in range(9):
            for i in range(9):
                if self.grid[j][i] == 0:
                    return [i, j]

        return None

    def solve(self):
        next_empty = self.return_first_empty()
        if next_empty:
            x, y = next_empty

            for i in range(1, 10):
                if self.check_valid(x, y, i):
                    self.grid[y][x] = i

                    if self.solve():
                        return True

                    self.grid[y][x] = 0

            return False
        else:
            return True


def main():
    puzzle = Sudoku(test1)
    puzzle.solve()

    for j in range(9):
        if j % 3 == 0 and j != 0:
            print("- - - - - - - - - - - -")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print(" | ", end="")
            if i == 8:
                print(puzzle.grid[j][i], end="\n")
            else:
                print(puzzle.grid[j][i], end=" ")


test1 = [[0, 0, 7, 9, 3, 0, 2, 5, 4],
         [9, 0, 0, 0, 0, 0, 8, 0, 0],
         [4, 0, 6, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 8, 1, 5, 6, 0],
         [0, 6, 0, 5, 0, 3, 0, 2, 0],
         [0, 5, 8, 4, 6, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 6, 0, 9],
         [0, 0, 2, 0, 0, 0, 0, 0, 5],
         [8, 9, 4, 0, 1, 5, 7, 0, 0]]

test2 = [[0 for _ in range(9)] for _ in range(9)]

main()
