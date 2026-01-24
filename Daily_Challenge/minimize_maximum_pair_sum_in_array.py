#1877. Minimize Maximum Pair Sum in Array

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Step 1: Sort the array to easily access smallest and largest elements
        nums.sort()
        
        max_pair_sum = 0
        n = len(nums)
        
        # Step 2: Iterate through the first half of the array
        # Pair the i-th smallest element with the i-th largest element
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            
            # Step 3: Update the maximum pair sum found so far
            max_pair_sum = max(max_pair_sum, current_sum)
            
        return max_pair_sum
    
# Time Complexity: O(n log n) due to sorting, where n is the length of the input array.
# Space Complexity: O(1) if we ignore the input storage, as we are sorting in place.