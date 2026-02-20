#696. Count Binary Substrings

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # XOR the number with itself shifted right by 1.
        # If bits are alternating, the result will be a sequence of all 1s (e.g., 111...1).
        x = n ^ (n >> 1)
        
        # Check if x contains all 1s.
        # If x is of the form 11...1, then x + 1 will be of the form 100...0.
        # Using bitwise AND, x & (x + 1) should result in 0.
        return (x & (x + 1)) == 0
    
# Time Complexity: O(1) since the operations are constant time.
# Space Complexity: O(1) since we are using a constant amount of space.