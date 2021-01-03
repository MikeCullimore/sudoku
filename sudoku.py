"""
sudoku.py

Sudoku solver based on Computerphile YouTube video.

https://www.youtube.com/watch?v=G_UYXzGuqvM
"""


# Example from video.
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def pprint(grid):
    for r in range(9):
        for c in range(9):
            value = grid[r][c]
            if value == 0:
                print(' ', end=' ')
            else:
                print(value, end=' ')
        print()


def possible(y, x, n):
    global grid  # todo: as arg?
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve():
    global grid  # todo: as arg?
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        
                        # # debugging
                        # pprint(grid)
                        # print()
                        
                        solve()

                        # Backtracking: this possibility didn't work out, so undo it.
                        grid[y][x] = 0
                return
    pprint(grid)
    # input('Search for other solutions?')
    return  # Stop after finding one solution.


solve()
