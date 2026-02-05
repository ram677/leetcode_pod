#3379. Transformed Array

from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(n):
            # In Python, the modulo operator % handles negative numbers correctly for circular arrays.
            # Example: (0 + (-1)) % 3 = 2.
            # This allows us to use one formula for both left (negative) and right (positive) moves.
            target_index = (i + nums[i]) % n
            result.append(nums[target_index])
            
        return result
    
# Time Complexity: O(n) - We iterate through the array once to construct the result.
# Space Complexity: O(n) - We create a new array to store the transformed values.