#36. Valid Sudoku

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track seen digits for each row, column, and 3x3 box.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through each cell of the 9x9 board.
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                
                # Skip empty cells.
                if digit == '.':
                    continue
                
                # 1. Check the current row for duplicates.
                if digit in rows[i]:
                    return False
                rows[i].add(digit)
                
                # 2. Check the current column for duplicates.
                if digit in cols[j]:
                    return False
                cols[j].add(digit)
                
                # 3. Check the current 3x3 sub-box for duplicates.
                box_index = (i // 3) * 3 + (j // 3)
                if digit in boxes[box_index]:
                    return False
                boxes[box_index].add(digit)
                
        # If the entire board is traversed without returning False, it is valid.
        return True

#Time Complexity: O(1)
#Space Complexity: O(1)