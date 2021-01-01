"""
sudoku.py

todo:
How to implement rules?
Web visualisation (React? Elm? Vanilla JS?).
"""


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example from card.
example = """
-36-----8
8---423-1
----3--9-
----8-42-
4-------5
-67-5----
-2--6----
6-849---2
1-----98-
"""

# Example puzzle used by Dad.
example2 = """
--7------
--9----54
16---49--
-------93
----694-7
--8-2----
--3-8-2--
-8-5----1
-1-97--6-
"""


class Cell:
    def __init__(self, value=None):
        if value is not None:
            self._value = value
            self._options = [value]
        else:
            self._value = value
            self._options = digits
    
    def __str__(self):
        if self._value is None:
            return ' '
        return str(self._value)


class Sudoku:
    """
    Sudoku puzzle.

    Convention: row 1 is the top, column 1 is the left.

    todo:
    Getter for a given number? ("Where are all the 1s?")
    Class for CellGroup, view into list of cells, with row, column and box as examples? Also cells in full puzzle?
        Print method.
    """

    def __init__(self, s=example):
        self._cells = []
        s = s.strip()
        rows = s.split()
        for row in rows:
            for col, c in enumerate(row):
                if c is '-':
                    value = None
                else:
                    try:
                        value = int(c)
                    except:
                        raise ValueError(f'Invalid character at row {row}, column {col}: {c}.')
                    if value not in digits:
                        raise ValueError(f'Invalid cell value: {value}.')
                self._cells.append(Cell(value))

    # def solve(self):
    #     pass
    
    def print(self):
        for row in digits:
            for col in digits:
                cell = self.cell(col, row)
                print(cell, end=' ')
            print()
    
    def cell(self, col, row):
        if col not in digits:
            raise ValueError(f'Invalid column index: {col}. Must be in 1-9.')
        if row not in digits:
            raise ValueError(f'Invalid row index: {row}. Must be in 1-9.')
        
        # Convert row and column to list index.
        index = (row-1)*9 + col - 1

        return self._cells[index]

    def col(self, i):
        if i not in digits:
            raise ValueError(f'Invalid column index: {i}. Must be in 1-9.')
        return [self.cell(i, row) for row in digits]
    
    def row(self, i):
        if i not in digits:
            raise ValueError(f'Invalid row index: {i}. Must be in 1-9.')
        return [self.cell(col, i) for col in digits]
    
    def box(self, i):
        if i not in digits:
            raise ValueError(f'Invalid box index: {i}. Must be in 1-9.')
        
        # Infer first column.
        # todo: replace with formula? (Less clear?)
        if i in [1, 4, 7]:
            c1 = 1
        elif i in [2, 5, 8]:
            c1 = 4
        else:  # (Relies on validation above.)
            c1 = 7
        
        # Infer first row.
        # todo: replace with formula? (Less clear?)
        if i in [1, 2, 3]:
            r1 = 1
        elif i in [4, 5, 6]:
            r1 = 4
        else:  # (Relies on validation above.)
            r1 = 7

        rows = [r1, r1+1, r1+2]
        cols = [c1, c1+1, c1+2]
        
        return [self.cell(col, row) for col in cols for row in rows]


def main():
    s = Sudoku(example)
    # s = Sudoku(example2)
    s.print()
    # print(len(s._cells))
    print(s._cells[1]._value)
    print(s.cell(2, 1)._value)
    # print(s.col(1))
    # print(s.row(1))
    print(s.box(1))


if __name__ == '__main__':
    main()