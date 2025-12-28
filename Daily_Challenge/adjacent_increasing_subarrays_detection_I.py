#3349. Adjacent Increasing Subarrays Detection I

from typing import List

class Solution:
    """
    Checks if there exist two adjacent strictly increasing subarrays, each of length k.
    The first subarray starts at index 'a' and the second starts at index 'b = a + k'.
    """
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # The first subarray of length k starts at index 'a'.
        # The second adjacent subarray of length k starts at index 'a + k'.
        # The combined length is 2*k. The ending index of the second subarray is (a + 2*k - 1).
        # This end index must be less than n.
        # So, a + 2*k - 1 < n  =>  a < n - 2*k + 1
        # The loop runs from a = 0 up to a = n - 2*k.
        
        # We only need to check starting positions 'a' such that the two full subarrays 
        # (total length 2*k) can fit in the 'nums' array.
        max_a = n - 2 * k
        
        # Helper function to check if a subarray of length k starting at 'start_index' is strictly increasing.
        def is_strictly_increasing(start_index: int) -> bool:
            # Check the k-1 gaps for strict inequality
            for i in range(k - 1):
                # Check nums[start_index + i] < nums[start_index + i + 1]
                if nums[start_index + i] >= nums[start_index + i + 1]:
                    return False
            return True

        # Iterate through all possible starting indices 'a' for the first subarray.
        for a in range(max_a + 1):
            # 1. Check the first subarray: nums[a...a + k - 1]
            first_is_increasing = is_strictly_increasing(a)
            
            if first_is_increasing:
                # 2. Check the second adjacent subarray: nums[a + k...a + 2*k - 1]
                b = a + k
                second_is_increasing = is_strictly_increasing(b)
                
                if second_is_increasing:
                    # Found a pair of adjacent strictly increasing subarrays
                    return True
        
        # If the loop finishes without finding such a pair
        return False
    
# Time Complexity: O(n * k), where n is the length of the nums array and k is the length of each subarray.
# Space Complexity: O(1) since we are using only a constant amount of extra space.