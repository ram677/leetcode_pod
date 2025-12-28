#2435. Paths in Matrix Whose Sum Is Divisible by K

class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][rem] stores the number of paths to (i, j) with path sum % k == rem
        # Initialize with zeros
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        
        # Base case: starting point (0, 0)
        initial_remainder = grid[0][0] % k
        dp[0][0][initial_remainder] = 1
        
        for i in range(m):
            for j in range(n):
                # Calculate the remainder contribution of the current cell
                current_val = grid[i][j] % k
                
                # If we can come from the top (i-1, j)
                if i > 0:
                    for rem in range(k):
                        # The new remainder at (i, j) will be (rem + current_val) % k
                        new_rem = (rem + current_val) % k
                        dp[i][j][new_rem] = (dp[i][j][new_rem] + dp[i-1][j][rem]) % MOD
                
                # If we can come from the left (i, j-1)
                if j > 0:
                    for rem in range(k):
                        new_rem = (rem + current_val) % k
                        dp[i][j][new_rem] = (dp[i][j][new_rem] + dp[i][j-1][rem]) % MOD
                        
        # The answer is the number of paths to the bottom-right cell (m-1, n-1)
        # with a total sum remainder of 0
        return dp[m-1][n-1][0]
    
# Time Complexity: O(m * n * k), where m is the number of rows, n is the number of columns, and k is the divisor.
# Space Complexity: O(m * n * k) for the dp array.