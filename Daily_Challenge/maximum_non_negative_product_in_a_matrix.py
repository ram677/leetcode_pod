#1594. Maximum Non Negative Product in a Matrix

from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize 2D arrays to store the max and min products up to each cell
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        # Base case: start position
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        # Initialize the first column (can only come from above)
        for i in range(1, m):
            val = max_dp[i-1][0] * grid[i][0]
            max_dp[i][0] = min_dp[i][0] = val
            
        # Initialize the first row (can only come from the left)
        for j in range(1, n):
            val = max_dp[0][j-1] * grid[0][j]
            max_dp[0][j] = min_dp[0][j] = val
            
        # DP transitions for the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Calculate all 4 possible products coming from top and left
                candidates = (
                    max_dp[i-1][j] * grid[i][j],
                    min_dp[i-1][j] * grid[i][j],
                    max_dp[i][j-1] * grid[i][j],
                    min_dp[i][j-1] * grid[i][j]
                )
                
                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
                
        # The result is stored in the bottom-right corner of max_dp
        ans = max_dp[-1][-1]
        
        # Return -1 if the max product is negative, else apply modulo
        if ans < 0:
            return -1
            
        return ans % (10**9 + 7)
    
# Time Complexity: O(m*n) where m and n are the dimensions of the grid, since we need to fill in the max_dp and min_dp arrays.
# Space Complexity: O(m*n) for the max_dp and min_dp arrays.