#1611. Minimum One Bit Operations to Make Integers Zero

from typing import List

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        
        # This loop computes ans = n ^ (n >> 1) ^ (n >> 2) ^ ...
        while n > 0:
            ans ^= n
            n >>= 1
            
        return ans
    
# Time Complexity: O(log n), where n is the input integer.
# Space Complexity: O(1)