from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Level: Medium

        Problem Statement
        -----------------

        Approach
        --------
        1. Create hashsets for the rows, columns, and 3x3 squares of the 
           Sudoku board.
        2. Iterate over each cell of the sudoku board and check if the value in
           the cell is already in its row, column, or 3x3 square hashset. If it
           is, then it is a conflict and the Sudoku is not valid.
        3. If the cell is valid, add the cell's value to its corresponding row,
           column, and 3x3 square set.

        Extra Info
        ----------
        We can think of all 3x3 squares as representable by their integer
        division value. For instance, all values in the bottom-most cell, when
        integer divided by 3, end up to be 2, which is the row and column index
        of the cell.

        Example: Cells board[0-2][0-2] would be in squares[(0, 0)] since at the
        very best, 2 // 3 is still 0. For a lower corner, like boards[6-8][6-8],
        the cells are at the least 6 // 3 = 2 and at max 8 // 3 = 2. So, they
        are contained in squares[(2, 2)]. We make the 81 cell Sudoku a 3x3
        again with each of its "cells" representing a 3x3.

        TC/SC
        -----
        TC: O(81)
        SC: O(n)
        '''
        cols, rows, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row // 3, col // 3)]:
                    return False
                
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        
        return True