#3350. Adjacent Increasing Subarrays Detection II

from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # l_end[i]: length of the strictly increasing subarray ending at index i.
        l_end = [0] * n
        l_end[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                l_end[i] = l_end[i - 1] + 1
            else:
                l_end[i] = 1

        # l_start[i]: length of the strictly increasing subarray starting at index i.
        l_start = [0] * n
        l_start[n - 1] = 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                l_start[i] = l_start[i + 1] + 1
            else:
                l_start[i] = 1

        max_k = 0
        # Iterate through all possible split points (between i-1 and i).
        for i in range(1, n):
            # The max k for this split is limited by the lengths of the
            # available increasing subarrays on either side.
            k = min(l_end[i - 1], l_start[i])
            max_k = max(max_k, k)

        return max_k
    
# Time Complexity: O(n), where n is the length of the nums array.
# Space Complexity: O(n) due to the additional arrays l_end and l_start.