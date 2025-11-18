#717. 1-bit and 2-bit Characters

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        
        # Iterate through the array, but stop before the very last index.
        # We want to see if our jumps land us ON the last index or PAST it.
        while i < n - 1:
            if bits[i] == 1:
                # Found a 2-bit character (10 or 11), skip the next bit.
                i += 2
            else:
                # Found a 1-bit character (0), move to next bit.
                i += 1
        
        # If i points exactly to the last index, the last character is 1-bit.
        return i == n - 1
    
# Time Complexity: O(n), where n is the length of the input list bits.
# Space Complexity: O(1), as we are using only a constant amount of extra space.