#1018. Binary Prefix Divisible By 5

from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        current_val = 0
        
        for bit in nums:
            # Update the current value by shifting left and adding the new bit.
            # We take modulo 5 at each step to prevent the number from growing too large.
            # (a * 2 + b) % 5 is equivalent to ((a % 5) * 2 + b) % 5
            current_val = (current_val * 2 + bit) % 5
            
            # If the remainder is 0, it's divisible by 5.
            answer.append(current_val == 0)
            
        return answer
    
# Time Complexity: O(n) where n is the number of bits in the input list.
# Space Complexity: O(n) for the output list storing boolean values.