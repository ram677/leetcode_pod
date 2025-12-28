#1493. Longest Subarray of 1's After Deleting One Element

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # shrink window if more than one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # window length minus 1 (delete one element)
            max_len = max(max_len, right - left + 1)

        return max_len - 1

#Time Complexity : O(n)
#Space Complexity : O(1)
#Where n is the number of elements in the input array.