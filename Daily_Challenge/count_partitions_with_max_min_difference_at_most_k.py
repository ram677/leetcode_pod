#3578. Count Partitions With Max-Min Difference at Most K

from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = nums.length if hasattr(nums, 'length') else len(nums)
        MOD = 10**9 + 7
        
        # dp[i] = number of ways to partition the prefix of length i
        # We need dp of size n + 1.
        dp = [0] * (n + 1)
        dp[0] = 1
        
        # prefix_dp[i] stores sum(dp[0]...dp[i-1])
        # This helps us calculate range sums in O(1)
        prefix_dp = [0] * (n + 2)
        prefix_dp[1] = 1  # Corresponds to sum including dp[0]
        
        max_d = deque() # Stores indices, values decreasing
        min_d = deque() # Stores indices, values increasing
        
        left = 0
        
        for i in range(n):
            # 1. Maintain Max Deque (Decreasing)
            while max_d and nums[max_d[-1]] <= nums[i]:
                max_d.pop()
            max_d.append(i)
            
            # 2. Maintain Min Deque (Increasing)
            while min_d and nums[min_d[-1]] >= nums[i]:
                min_d.pop()
            min_d.append(i)
            
            # 3. Shrink window from the left if max - min > k
            while nums[max_d[0]] - nums[min_d[0]] > k:
                left += 1
                # Remove indices that are now out of the window
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()
            
            # 4. Calculate DP value
            # The valid last segments are nums[j...i] where left <= j <= i.
            # This means the previous partition ended at j.
            # We need sum(dp[j]) for left <= j <= i.
            
            # prefix_dp[x] = sum(dp[0]...dp[x-1])
            # sum(dp[left]...dp[i]) = prefix_dp[i+1] - prefix_dp[left]
            
            current_ways = (prefix_dp[i + 1] - prefix_dp[left]) % MOD
            dp[i + 1] = current_ways
            
            # Update prefix sum for the next iteration
            prefix_dp[i + 2] = (prefix_dp[i + 1] + current_ways) % MOD
            
        return dp[n]
    
#Time Complexity: O(n), where n is the length of the input list.
#Space Complexity: O(n), for the dp and prefix_dp arrays.