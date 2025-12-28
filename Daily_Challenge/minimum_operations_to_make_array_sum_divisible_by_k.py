#3512. Minimum Operations to Make Array Sum Divisible by K

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
    
# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(1), since we are using a constant amount of space for the calculation.