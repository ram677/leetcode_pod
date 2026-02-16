#190. Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Shift result to the left to open up the least significant bit
            result = (result << 1)
            
            # Get the last bit of n and add it to result
            if n & 1:
                result += 1
            
            # Shift n to the right to process the next bit
            n = (n >> 1)
            
        return result

# Time Complexity: O(1) since we are always processing 32 bits, which is a constant.
# Space Complexity: O(1) since we are using a constant amount of space for the result and temporary variables.