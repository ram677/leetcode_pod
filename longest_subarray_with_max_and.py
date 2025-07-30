from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_len = 0
        curr_len = 0

        for num in nums:
            if num == max_val:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0
        
        return max_len
    
# Time Complexity: O(n)
# Space Complexity: O(1)    
# n is the length of the input list nums, i.e., the number of elements in the array.