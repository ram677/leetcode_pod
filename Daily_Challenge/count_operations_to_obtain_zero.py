#2169. Count Operations to Obtain Zero

from typing import List

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        # Initialize the operation counter
        operations_count = 0
        
        # Loop until one of the numbers becomes zero
        while num1 > 0 and num2 > 0:
            
            # Perform the subtraction based on which number is larger
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
                
            # Count this as one operation
            operations_count += 1
            
        return operations_count
    
# Time Complexity: O(max(num1, num2)), where num1 and num2 are the input integers.
# Space Complexity: O(1)