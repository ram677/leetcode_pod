#2654. Minimum Number of Operations to Make All Array Elements Equal to 1

import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Check if 1s already exist
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count
        
        min_ops_to_make_one = float('inf')
        
        # Step 2: Find the shortest subarray with GCD == 1
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = math.gcd(current_gcd, nums[j])
                
                if current_gcd == 1:
                    # The number of operations to make a 1 from this subarray 
                    # is the number of edges (j - i).
                    min_ops_to_make_one = min(min_ops_to_make_one, j - i)
                    # Once we hit 1, extending the subarray further won't reduce the cost.
                    break 
        
        # Step 3: Calculate final result
        if min_ops_to_make_one == float('inf'):
            return -1
        
        # Cost = ops to get the first 1 + ops to spread it to the other n-1 elements
        return min_ops_to_make_one + (n - 1)
    
# Time Complexity: O(n^2 * log(max(nums)))), where n is the length of nums. The log factor comes from the GCD computation.
# Space Complexity: O(1) as we are using only a constant amount of extra space.