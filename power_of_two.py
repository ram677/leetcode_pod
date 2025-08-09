#231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# Time Complexity: O(1) since the bitwise operations are constant time.
# Space Complexity: O(1) as no additional space is used.    
# Note: The solution checks if n is a power of two using a bitwise operation.   