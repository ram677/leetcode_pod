#3190. Find Minimum Operations to Make All Elements Divisible by Three

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        
        for num in nums:
            if num % 3 != 0:
                # If remainder is 1 or 2, it takes 1 operation to fix.
                operations += 1
                
        return operations
    
# Time Complexity: O(n) where n is the number of elements in the list.
# Space Complexity: O(1) since we are using a constant amount of extra space.