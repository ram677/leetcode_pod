#2787. Ways to Express an Integer as Sum of Powers

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Generate possible x-th powers
        powers = []
        i = 1
        while i**x <= n:
            powers.append(i**x)
            i += 1
        
        # Step 2: DP array
        dp = [0] * (n + 1)
        dp[0] = 1  # one way to make sum 0 (choose nothing)
        
        # Step 3: Process each power
        for p in powers:
            for t in range(n, p - 1, -1):
                dp[t] = (dp[t] + dp[t - p]) % MOD
        
        return dp[n]
    
#Time complexity : O(m*n)
#Space complexity : O(n)
#Where m is the number of x-th powers less than or equal to n, and n is the target integer.
