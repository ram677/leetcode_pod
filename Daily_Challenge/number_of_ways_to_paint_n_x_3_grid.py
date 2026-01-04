#1411. Number of Ways to Paint N × 3 Grid

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Initial state for n = 1
        # 'abc' is the number of ways to paint a row with 3 distinct colors
        # 'aba' is the number of ways to paint a row with 2 distinct colors
        abc = 6
        aba = 6
        
        for _ in range(n - 1):
            # Calculate next counts based on transition rules
            new_abc = (2 * abc + 2 * aba) % MOD
            new_aba = (2 * abc + 3 * aba) % MOD
            
            abc = new_abc
            aba = new_aba
            
        return (abc + aba) % MOD
    
# Time Complexity: O(n), where n is the number of rows in the grid.
# Space Complexity: O(1). 