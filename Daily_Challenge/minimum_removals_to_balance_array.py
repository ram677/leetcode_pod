#3634. Minimum Removals to Balance Array

from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_len = 0
        left = 0
        
        for right in range(n):
            # While the window is invalid (max > min * k), shrink from the left
            while nums[right] > nums[left] * k:
                left += 1
            
            # Update the maximum length of a valid window found so far
            max_len = max(max_len, right - left + 1)
            
        return n - max_len
    
# Time Complexity: O(n log n) - Sorting the array takes O(n log n), and the two-pointer traversal takes O(n).
# Space Complexity: O(1) - We are using only a constant amount of extra space for the two pointers and variables.