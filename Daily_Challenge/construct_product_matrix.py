#2906. Construct Product Matrix

from typing import List

class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        
        # Initialize the result matrix
        p = [[0] * m for _ in range(n)]
        
        # Step 1: Forward pass (Prefix products)
        # We traverse the grid from top-left to bottom-right.
        # 'pref' keeps track of the product of all elements visited BEFORE the current cell.
        pref = 1
        for r in range(n):
            for c in range(m):
                # Store the prefix product in the result matrix
                p[r][c] = pref
                # Update the running prefix product with the current cell's value
                pref = (pref * grid[r][c]) % MOD
                
        # Step 2: Backward pass (Suffix products)
        # We traverse the grid from bottom-right to top-left.
        # 'suff' keeps track of the product of all elements visited AFTER the current cell.
        suff = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                # Multiply the existing prefix product by the current suffix product
                # This effectively gives us the product of everything EXCEPT grid[r][c]
                p[r][c] = (p[r][c] * suff) % MOD
                # Update the running suffix product with the current cell's value
                suff = (suff * grid[r][c]) % MOD
                
        return p
    
# Time Complexity: O(n*m) where n and m are the dimensions of the grid, since we traverse the grid twice (forward and backward).
# Space Complexity: O(n*m) for the result matrix 'p'. The additional space used for 'pref' and 'suff' is O(1).