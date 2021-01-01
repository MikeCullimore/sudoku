"""
sudoku.py
"""


# Example from card.
example = [
    [None, 3, 6, None, None, None, None, None, 8],
    [8, None, None, None, 4, 2, 3, None, 1],
    [None, None, None, None, 3, None, None, 9, None],
    [None, None, None, None, 8, None, 4, 2, None],
    [4, None, None, None, None, None, None, None, 5],
    [None, 6, 7, None, 5, None, None, None, None],
    [None, 2, None, None, 6, None, None, None, None],
    [6, None, 8, 4, 9, None, None, None, 2],
    [1, None, None, None, None, None, 9, 8, None]
]


# Example puzzle used by Dad.
example2 = [
    [None, None, 7, None, None, None, None, None, None],
    [None, None, 9, None, None, None, None, 5, 4],
    [1, 6, None, None, None, 4, 9, None, None],
    [None, None, None, None, None, None, None, 9, 3],
    [None, None, None, None, 6, 9, 4, None, 7],
    [None, None, 8, None, 2, None, None, None, None],
    [None, None, 3, None, 8, None, 2, None, None],
    [None, 8, None, 5, None, None, None, None, 1],
    [None, 1, None, 9, 7, None, None, 6, None]
]

class Sudoku:
    def __init__(self, cells=example2):
        self._cells = cells
    
    def print(self):
        for row in self._cells:
            for cell in row:
                if cell is None:
                    print(' ', end=' ')
                    continue
                print(cell, end=' ')
            print()

    def solve(self):
        pass


def main():
    s = Sudoku()
    s.print()


if __name__ == '__main__':
    main()