#3507. Minimum Pair Removal to Sort Array I

from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Helper function to check if the array is non-decreasing
        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        # If initially sorted, 0 operations needed
        if is_sorted(nums):
            return 0
        
        operations = 0
        current_nums = list(nums)
        
        while len(current_nums) > 1:
            # 1. Find the adjacent pair with the minimum sum
            min_sum = float('inf')
            min_index = -1
            
            for i in range(len(current_nums) - 1):
                pair_sum = current_nums[i] + current_nums[i+1]
                
                # Check for strictly smaller sum to satisfy "leftmost" tie-breaker.
                # If pair_sum == min_sum, we ignore it to keep the left-most index.
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_index = i
            
            # 2. Merge the pair: Replace nums[min_index] and nums[min_index+1] with their sum
            new_val = current_nums[min_index] + current_nums[min_index+1]
            
            # Slicing creates the new array state
            current_nums = current_nums[:min_index] + [new_val] + current_nums[min_index+2:]
            operations += 1
            
            # 3. Check if the array is now sorted
            if is_sorted(current_nums):
                return operations
                
        return operations
    
# Time complexity: O(n^2) in the worst case, where n is the length of nums.
# Space complexity: O(n) for storing the current state of the array.