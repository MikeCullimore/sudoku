"""
sudoku.py

todo:
Logging (to conveniently show/hide debug info.)
How to implement rules? As Class?
Visualisation:
    Not only current state but also options.
    Web? (React? Elm? Vanilla JS?)
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

# Example from Dad.
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
        self._value = value
        if value is None:    
            self._options = digits.copy()  # Deep copy (else we'd be mutating digits).
        else:
            if value not in digits:
                raise ValueError(f'Invalid cell value: {value}.')
            self._options = [value]
    
    def __str__(self):
        if self.known():
            return str(self.value)
        return ' '
        
    
    def eliminate(self, option):
        # If cell known already, return.
        if self.known():
            return
        
        try:
            self._options.remove(option)
        except ValueError:
            # print(f'(Option {option} has been removed already).')
            return
        
        if len(self._options) == 1:
            self._value = self._options[0]
            print(f'Solved cell: value = {self.value}')  # debugging

    def known(self):
        return self.value is not None
    
    @property
    def value(self):
        return self._value


class Sudoku:
    """
    Sudoku puzzle.

    Convention: row 1 is the top, column 1 is the left.

    todo:
    Getters for non-empty cells in given group?
    Function to convert cell index to col and row? (Inverse of what we have.)
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
                self._cells.append(Cell(value))

    # def solve(self):
    #     pass
    
    def print(self):
        for row in digits:
            for col in digits:
                print(self.cell(col, row), end=' ')
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
    
    def block(self, b):
        if b not in digits:
            raise ValueError(f'Invalid box index: {b}. Must be in 1-9.')
        
        # Infer first column.
        # todo: replace with formula? (Less clear?)
        if b in [1, 4, 7]:
            c1 = 1
        elif b in [2, 5, 8]:
            c1 = 4
        else:  # (Relies on validation above.)
            c1 = 7
        
        # Infer first row.
        # todo: replace with formula? (Less clear?)
        if b in [1, 2, 3]:
            r1 = 1
        elif b in [4, 5, 6]:
            r1 = 4
        else:  # (Relies on validation above.)
            r1 = 7

        rows = [r1, r1+1, r1+2]
        cols = [c1, c1+1, c1+2]
        
        return [self.cell(col, row) for col in cols for row in rows]
    
    def cols(self):
        """Iterator over columns."""
        for c in digits:
            yield self.col(c)
    
    def rows(self):
        """Iterator over rows."""
        for r in digits:
            yield self.row(r)
    
    def blocks(self):
        """Iterator over blocks."""
        for b in digits:
            yield self.block(b)


def main():
    s = Sudoku(example)
    # s = Sudoku(example2)
    
    # s.print()
    
    # Debugging.
    # print(len(s._cells))
    # print(s._cells[1].value)
    # print(s.cell(2, 1).value)
    # print(s.col(1))
    # print(s.row(1))
    # print(s.box(1))

    # Solve: work in progress!
    # todo: apply col, row and box rules at each cell.
    # todo: keep iterating until no further changes.
    # todo: Don't Repeat Yourself: one neighbour comparison for all rules.

    # Logic for second pass:
    # Column rule:
        # Iterate over columns
        # Separate into known and unknown cells.
        # Make list of values of known cells.
        # Eliminate those values from each unknown cell.
    # Row rule: likewise.
    # Box rule: likewise.
    indices = []
    values = []
    for i, col in enumerate(s.cols()):
        c = i + 1
        for j, cell in enumerate(col):
            r = j + 1
            print(f'At ({c}, {r})')
            if cell.known():
                values.append(cell.value)
            else:
                indices.append((c, r))
        for value in values:
            for c, r in indices:
                s.cell(c, r).eliminate(value)

    # for r in digits:
    #     for c in digits:
    #         # print(f'At ({c}, {r})')
            
    #         # Column rule.
    #         for neighbour in s.col(c):
    #             # Do not compare cell with itself.
    #             if neighbour is s.cell(c, r):
    #                 continue
                
    #             # If neighbour is known, eliminate option for this cell.
    #             # todo: check here that it has not been eliminated already? Can then track changes.
    #             if neighbour.value is not None:
    #                 # print(f'Cell ({c}, {r}) can\'t be {neighbour.value} (column rule).')
    #                 s.cell(c, r).eliminate(neighbour.value)
            
    #         # Row rule.
    #         for neighbour in s.row(c):
    #             # Do not compare cell with itself.
    #             if neighbour is s.cell(c, r):
    #                 continue
                
    #             # If neighbour is known, eliminate option for this cell.
    #             # todo: check here that it has not been eliminated already? Can then track changes.
    #             if neighbour.value is not None:
    #                 # print(f'Cell ({c}, {r}) can\'t be {neighbour.value} (row rule).')
    #                 s.cell(c, r).eliminate(neighbour.value)
            
    #         # todo: box rule (modify getter?).
    
    # # Print status after rules applied.
    # print()
    # s.print()


if __name__ == '__main__':
    main()
