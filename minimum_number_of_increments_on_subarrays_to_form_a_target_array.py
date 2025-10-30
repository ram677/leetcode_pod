#1526. Minimum Number of Increments on Subarrays to Form a Target Array

from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # The number of operations starts with the value of the first element,
        # as we need to build it up from zero.
        operations = target[0]
        
        # Iterate through the array starting from the second element.
        for i in range(1, len(target)):
            # If the current element is greater than the previous one,
            # we need additional operations to cover the difference.
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
                
        return operations
    
# Time Complexity: O(n), where n is the length of the target array.
# Space Complexity: O(1), as we are using a constant amount of extra space.