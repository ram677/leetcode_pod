#498. Diagonal Traverse

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = [0] * (m * n)
        row, col = 0, 0
        going_up = True

        for i in range(m * n):
            result[i] = mat[row][col]
            
            # Prepare for the next element
            if going_up:
                # If we hit the right boundary, move down and flip direction
                if col == n - 1:
                    row += 1
                    going_up = False
                # If we hit the top boundary, move right and flip direction
                elif row == 0:
                    col += 1
                    going_up = False
                # Otherwise, move up-right
                else:
                    row -= 1
                    col += 1
            else:  # Going down-left
                # If we hit the bottom boundary, move right and flip direction
                if row == m - 1:
                    col += 1
                    going_up = True
                # If we hit the left boundary, move down and flip direction
                elif col == 0:
                    row += 1
                    going_up = True
                # Otherwise, move down-left
                else:
                    row += 1
                    col -= 1
        
        return result
    
#Time Complexity : O(m * n)
#Space Complexity : O(1)
#Where m is the number of rows and n is the number of columns in the matrix.