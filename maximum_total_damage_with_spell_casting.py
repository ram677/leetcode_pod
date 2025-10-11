#3186. Maximum Total Damage With Spell Casting

import collections
import bisect
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # 1. Count frequencies and get a sorted list of unique powers.
        counts = collections.Counter(power)
        unique_powers = sorted(counts.keys())
        n = len(unique_powers)
        
        # dp[i] will store the maximum damage considering powers up to unique_powers[i].
        dp = [0] * n
        
        # Base case: For the first unique power, we must take it.
        dp[0] = unique_powers[0] * counts[unique_powers[0]]
        
        for i in range(1, n):
            p = unique_powers[i]
            
            # Option 1: Skip the current power 'p'.
            # The damage is the best we could do with the previous powers.
            damage_skip = dp[i-1]
            
            # Option 2: Take the current power 'p'.
            damage_take = p * counts[p]
            
            # Find the last compatible power (power < p - 2).
            # We search for the insertion point of p - 2. The index before that
            # gives us the last power that is strictly less than p - 2.
            target = p - 2
            j = bisect.bisect_left(unique_powers, target) - 1
            
            # If a compatible previous power exists, add its max damage.
            if j >= 0:
                damage_take += dp[j]
                
            # The max damage at this step is the max of the two options.
            dp[i] = max(damage_skip, damage_take)
            
        return dp[n-1]
    
# Time Complexity: O(n log n) due to sorting and binary search.
# Space Complexity: O(n) for the dp array and unique powers list.