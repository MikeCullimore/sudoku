"""
sudoku.py

Sudoku solver based on Computerphile YouTube video. (Object-oriented version.)

https://www.youtube.com/watch?v=G_UYXzGuqvM
"""


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

# Example from video.
example3 = """
53--7----
6--195---
-98----6-
8---6---3
4--8-3--1
7---2---6
-6----28-
---419--5
----8--79
"""

class Sudoku:
    """
    Sudoku puzzle.

    Convention: row 0 is the top, column 0 is the left.
    """

    def solve(self):
        for r in range(9):
            for c in range(9):
                if self._cells[r][c] == 0:
                    for n in range(1, 10):
                        if self.possible(c, r, n):
                            self._cells[r][c] = n
                            
                            # # debugging
                            # self.print()
                            # print()
                            
                            self.solve()

                            # Backtracking: this possibility didn't work out, so undo it.
                            self._cells[r][c] = 0
                    return
        self.print()
        return
    
    def possible(self, c, r, n):
        """Is the number n possible at column c, row r?"""
        # Row rule.
        for i in range(9):
            if self._cells[r][i] == n:
                return False
        
        # Column rule.
        for i in range(9):
            if self._cells[i][c] == n:
                return False
        
        # Box rule.
        c0 = (c//3)*3
        r0 = (r//3)*3
        for i in range(3):
            for j in range(3):
                if self._cells[r0+i][c0+j] == n:
                    return False

        return True

    def print(self):
        for r in range(9):
            for c in range(9):
                value = self._cells[r][c]
                if value == 0:
                    print(' ', end=' ')
                else:
                    print(value, end=' ')
            print()
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            s = f.read()
        return cls(s)
    
    def __init__(self, s=example):
        """
        todo: input validation e.g. enforce 9 rows and columns.
        """
        self._cells = []
        s = s.strip()
        rows = s.split()
        for row in rows:
            r = []
            for col, c in enumerate(row):
                if c == '-':
                    value = 0
                else:
                    try:
                        value = int(c)
                    except:
                        raise ValueError(f'Invalid character at row {row}, column {col}: {c}.')
                r.append(value)
            self._cells.append(r)


def main():
    # Read from string.
    # puzzle = example3
    # s = Sudoku(example3)

    # Read from file.
    s = Sudoku.from_file('puzzles/puzzle4.txt')
    
    # s.print()
    # print(s._cells)
     
    s.solve()
    # s.print()
    
    # Debugging.
    # print(len(s._cells))
    # print(s._cells[1].value)
    # print(s.cell(2, 1).value)
    # print(s.col(1))
    # print(s.row(1))
    # print(s.box(1))


if __name__ == '__main__':
    main()
