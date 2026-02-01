#3010. Divide an Array Into Subarrays With Minimum Cost I

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # The first element is always the cost of the first subarray.
        # We then simply need the two smallest elements from the rest of the array
        # to serve as the cheapest heads for the 2nd and 3rd subarrays.
        return nums[0] + sum(sorted(nums[1:])[:2])
    
# Time Complexity: O(n log n) due to sorting the subarray.
# Space Complexity: O(1) if we ignore the input storage, otherwise O(n) for the sorted copy.