'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

    The given board contain only digits 1-9 and the character '.'.
    You may assume that the given Sudoku puzzle will have a single unique solution.
    The given board size is always 9x9.
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_empty_cell(row, col):
            return board[row][col] == "."
        
        def can_place_digit(row, col, digit):
            return (digit not in rows[row] and
                    digit not in cols[col] and
                    digit not in subgrids[row // 3][col // 3])
            
        def place_digit(row, col, digit):
            board[row][col] = digit
            cols[col].add(digit)
            rows[row].add(digit)
            subgrids[row // 3][col // 3].add(digit)
            
        def remove_digit(row, col):
            cols[col].remove(board[row][col])
            rows[row].remove(board[row][col])
            subgrids[row // 3][col // 3].remove(board[row][col])
            board[row][col] = "."
            
        def next_empty_row_col(row, col):
            while row < len(board) and col < len(board[0]) and not is_empty_cell(row,col):
                if col == len(board[0]) - 1:
                    row,col = row+1,0
                else:
                    row,col = row,col+1
            return row,col
        
        def solve(row, col):
            if row >= len(board):
                return True
            
            for digit in [str(num) for num in range(1,10)]:
                if can_place_digit(row,col,digit):
                    place_digit(row,col,digit)
                    next_row,next_col = next_empty_row_col(row,col)
                    if solve(next_row, next_col):
                        return True
                    remove_digit(row,col) #if solution not found, backtrack
            return False
        
        
        #Initialize 3 sets with the existing numbers on the board
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        subgrids = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(len(board)):
            for j in range(len(board)):
                if not is_empty_cell(i, j):
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    subgrids[i // 3][j // 3].add(board[i][j])
        
        #find the 1st empty cell and start there!
        start_row, start_col = next_empty_row_col(0,0)       
        solve(start_row, start_col)
