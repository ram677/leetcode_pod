#37. Sudoku Solver

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Initialize arrays to track used numbers
        row_used = [[False] * 9 for _ in range(9)]
        col_used = [[False] * 9 for _ in range(9)]
        box_used = [[False] * 9 for _ in range(9)]
        
        # Preprocess the board to mark used numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    row_used[i][num] = True
                    col_used[j][num] = True
                    box_index = (i // 3) * 3 + (j // 3)
                    box_used[box_index][num] = True
        
        # Define the backtracking function
        def backtrack():
            # Find the cell with the fewest possibilities
            min_count = 10
            min_i, min_j = -1, -1
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        count = 0
                        for num in range(9):
                            if not row_used[i][num] and not col_used[j][num] and not box_used[(i//3)*3 + j//3][num]:
                                count += 1
                        if count == 0:
                            return False
                        if count < min_count:
                            min_count = count
                            min_i, min_j = i, j
            
            # If no empty cell found, the board is solved
            if min_i == -1:
                return True
            
            # Try all possible numbers for the selected cell
            for num in range(9):
                if not row_used[min_i][num] and not col_used[min_j][num] and not box_used[(min_i//3)*3 + min_j//3][num]:
                    digit = str(num + 1)
                    board[min_i][min_j] = digit
                    row_used[min_i][num] = True
                    col_used[min_j][num] = True
                    box_used[(min_i//3)*3 + min_j//3][num] = True
                    
                    if backtrack():
                        return True
                    
                    # Backtrack
                    board[min_i][min_j] = '.'
                    row_used[min_i][num] = False
                    col_used[min_j][num] = False
                    box_used[(min_i//3)*3 + min_j//3][num] = False
            
            return False
        
        backtrack()

#Time Complexity: O(9^n) in the worst case, where n is the size of the board (9 for standard Sudoku)
#Space Complexity: O(1) since the board size is fixed (9x9)