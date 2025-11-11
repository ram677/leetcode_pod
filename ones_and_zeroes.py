#474. Ones and Zeroes

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # dp[j][k] will store the max subset size with at most
        # j zeros and k ones.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Pre-calculating counts is slightly cleaner, though not strictly necessary.
        counts = [(s.count('0'), s.count('1')) for s in strs]
        
        for zeros, ones in counts:
            # We iterate backward from the max budgets down to the
            # "cost" of the current string.
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    # We have two choices:
                    # 1. Don't take this string (value is dp[j][k])
                    # 2. Take this string (value is 1 + dp[j - zeros][k - ones])
                    dp[j][k] = max(
                        dp[j][k], 
                        1 + dp[j - zeros][k - ones]
                    )
                    
        # The final answer is the max subset size we can get
        # with the full budgets m and n.
        return dp[m][n]
    
# Time Complexity: O(L * m * n), where L is the number of strings in strs, and m and n are the given limits on zeros and ones respectively.
# Space Complexity: O(m * n) for the dp array.