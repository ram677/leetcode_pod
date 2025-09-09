#2327. Number of People Aware of a Secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] stores the number of people who learned the secret on day i.
        dp = [0] * (n + 1)
        dp[1] = 1
        
        # `sharing` tracks the number of people who are currently sharing the secret.
        sharing = 0
        
        for i in range(2, n + 1):
            # People who learned the secret on day i - delay start sharing today.
            if i - delay >= 1:
                sharing = (sharing + dp[i - delay]) % MOD
            
            # People who learned the secret on day i - forget forget it today.
            # They were sharing yesterday, but not today.
            if i - forget >= 1:
                sharing = (sharing - dp[i - forget] + MOD) % MOD
            
            # The number of new people on day i is equal to the number of people
            # who are sharing today.
            dp[i] = sharing
            
        # The total number of people aware on day n are those who have not forgotten yet.
        # This is the sum of dp[i] for i from (n - forget + 1) to n.
        total_aware = 0
        for i in range(n - forget + 1, n + 1):
            total_aware = (total_aware + dp[i]) % MOD
            
        return total_aware

#Time Complexity: O(n)
#Space Complexity: O(n)
#Where n is the number of days.