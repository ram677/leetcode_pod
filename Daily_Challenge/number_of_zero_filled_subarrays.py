#2348. Number of Zero-Filled Subarrays

from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                res += count
            else:
                count = 0
        return res

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the length of the input array.