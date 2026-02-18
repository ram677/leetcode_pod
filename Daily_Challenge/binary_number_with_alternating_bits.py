#693. Binary Number with Alternating Bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR the number with itself shifted right by 1.
        # If bits are alternating, the result will be a sequence of all 1s (e.g., 111...1).
        x = n ^ (n >> 1)
        
        # Check if x contains all 1s.
        # If x is of the form 11...1, then x + 1 will be of the form 100...0.
        # Using bitwise AND, x & (x + 1) should result in 0.
        return (x & (x + 1)) == 0