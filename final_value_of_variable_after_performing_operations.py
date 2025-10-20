#2011. Final Value of Variable After Performing Operations

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Initialize the variable X to 0.
        x = 0
        
        # Loop through each operation in the list.
        for op in operations:
            # If '+' is in the operation string, it's an increment.
            if '+' in op:
                x += 1
            # Otherwise, it must be a decrement.
            else:
                x -= 1
                
        # Return the final value of X.
        return x
    
#Time Complexity: O(n) where n is the number of operations.
#Space Complexity: O(1) since we are using a constant amount of space.