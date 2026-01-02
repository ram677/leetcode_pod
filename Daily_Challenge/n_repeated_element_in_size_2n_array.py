#961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1  

# Time Complexity: O(n), where n is the length of the input array nums.
# Space Complexity: O(n) in the worst case, if all elements are unique until the repeated one is found.