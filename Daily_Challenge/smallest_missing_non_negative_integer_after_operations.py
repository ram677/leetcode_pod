#2598. Smallest Missing Non-negative Integer After Operations

from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """
        Calculates the maximum possible MEX by leveraging modular arithmetic.
        """
        
        # Step 1: Count the frequency of each remainder modulo `value`.
        counts = [0] * value
        for num in nums:
            remainder = num % value
            counts[remainder] += 1
            
        # Step 2: Greedily try to form the sequence 0, 1, 2, ...
        mex = 0
        while True:
            # Determine the required remainder for the current target `mex`.
            required_remainder = mex % value
            
            # Check if we have an available number that can be transformed.
            if counts[required_remainder] > 0:
                # If yes, "use" one number from that remainder group.
                counts[required_remainder] -= 1
                # And move on to the next integer.
                mex += 1
            else:
                # If no, we cannot form the current `mex`. It's our answer.
                break
                
        return mex