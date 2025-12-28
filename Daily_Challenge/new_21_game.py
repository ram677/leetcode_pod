#837. New 21 Game

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Edge case: if k is 0, Alice never draws, so she has 0 points
        if k == 0:
            return 1.0
        
        # Edge case: if k + maxPts - 1 <= n, Alice can never exceed n
        if k + maxPts - 1 <= n:
            return 1.0
        
        # dp[i] represents the probability of getting <= n points starting from i points
        dp = [0.0] * (k + maxPts)
        
        # Base cases: if we already have >= k points, we stop
        # If we have i points where k <= i <= n, probability is 1
        # If we have i points where i > n, probability is 0
        window_sum = 0.0
        for i in range(k, k + maxPts):
            if i <= n:
                dp[i] = 1.0
            window_sum += dp[i]
        
        # Fill dp table backwards from k-1 to 0 using sliding window
        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts
            
            # Update sliding window for next iteration
            # Remove dp[i + maxPts] from window (if it exists)
            if i + maxPts < len(dp):
                window_sum -= dp[i + maxPts]
            # Add dp[i] to window
            window_sum += dp[i]

        return dp[0]
    
"""
Complexity Analysis:

Time: O(k + maxPts) - each element is added/removed from window exactly once
Space: O(k + maxPts) - for the DP array

"""