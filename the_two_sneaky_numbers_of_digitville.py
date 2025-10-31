#3289. The Two Sneaky Numbers of Digitville

from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        sneaky_numbers = []
        
        for num in nums:
            if num in seen:
                # If we've seen this number before, it's a sneaky duplicate.
                sneaky_numbers.append(num)
            else:
                # Otherwise, add it to the set of numbers we've seen.
                seen.add(num)
                
        return sneaky_numbers
    
# Time Complexity: O(n), where n is the length of the nums array.
# Space Complexity: O(n), in the worst case we might store all numbers in the seen set.
