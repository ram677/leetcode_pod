#3381. Maximum Subarray Sum With Length Divisible by K

import math

class Solution:
    def maxSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Initialize min_prefix array to infinity.
        # This array stores the minimum prefix sum encountered for each remainder index.
        min_prefix = [math.inf] * k
        
        # Base case: A prefix sum of 0 exists at index -1 (conceptually), 
        # which corresponds to remainder 0.
        min_prefix[0] = 0
        
        current_prefix_sum = 0
        max_sum = -math.inf
        
        for i in range(n):
            current_prefix_sum += nums[i]
            
            # The current ending index is 'i'. In 1-based length logic, this is length i+1.
            # We need to find a previous prefix index 'prev_idx' such that:
            # (current_idx - prev_idx) % k == 0
            # This implies current_idx % k == prev_idx % k
            # Here, the current position in the prefix sum array corresponds to index (i + 1).
            rem = (i + 1) % k
            
            # If we have seen a valid prefix sum with the same remainder before
            if min_prefix[rem] != math.inf:
                current_subarray_sum = current_prefix_sum - min_prefix[rem]
                if current_subarray_sum > max_sum:
                    max_sum = current_subarray_sum
            
            # Update the minimum prefix sum for this remainder
            if current_prefix_sum < min_prefix[rem]:
                min_prefix[rem] = current_prefix_sum
                
        # If max_sum is still -inf (though constraints say n >= k, so a solution should exist),
        # return it or handle accordingly. With constraints, it will always find a value.
        return max_sum
    
# Time Complexity: O(n), where n is the length of the input array nums.
# Space Complexity: O(k) for the min_prefix array.