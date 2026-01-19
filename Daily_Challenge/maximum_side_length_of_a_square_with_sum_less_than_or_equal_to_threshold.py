#1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        
        # --- Step 1: Build 2D Prefix Sum Matrix ---
        # P[i][j] will store the sum of the rectangle from (0,0) to (i-1, j-1)
        # We use dimensions (rows + 1) x (cols + 1) to handle boundaries easily (1-based indexing).
        P = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # Current cell value + sum above + sum left - overlap (top-left diagonal)
                P[r][c] = mat[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]
        
        # --- Step 2: Iterate and Find Max Side Length ---
        current_max = 0
        
        # Iterate through every cell treating it as the bottom-right corner of a square
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                # We only care if we can find a square larger than what we already found.
                # Let's check a square of size (current_max + 1).
                target_len = current_max + 1
                
                # Check bounds: can a square of 'target_len' fit ending at (r, c)?
                if r >= target_len and c >= target_len:
                    # Calculate sum of square of size 'target_len' ending at (r, c)
                    # Top-left corner of this square in 1-based P coordinates is (r - target_len, c - target_len)
                    r_start = r - target_len
                    c_start = c - target_len
                    
                    square_sum = P[r][c] - P[r_start][c] - P[r][c_start] + P[r_start][c_start]
                    
                    if square_sum <= threshold:
                        current_max += 1
                        
        return current_max
    
# Time complexity: O(rows * cols), where rows and cols are the dimensions of the matrix.
# Space complexity: O(rows * cols) for the prefix sum matrix.