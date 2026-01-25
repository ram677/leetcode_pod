#1984. Minimum Difference Between Highest and Lowest of K Scores

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # If we only need to pick 1 student, the difference is always 0
        if k == 1:
            return 0
            
        # Step 1: Sort the scores to group close values together
        nums.sort()
        
        min_diff = float('inf')
        
        # Step 2: Use a sliding window of size k
        # The window starts at index 'i' and ends at 'i + k - 1'
        # We iterate until the window hits the end of the array
        for i in range(len(nums) - k + 1):
            high = nums[i + k - 1]
            low = nums[i]
            
            current_diff = high - low
            min_diff = min(min_diff, current_diff)
            
        return min_diff
    
# Time Complexity: O(n log n) due to sorting, where n is the length of the input array.
# Space Complexity: O(1) if we ignore the input storage, as we are sorting in place.