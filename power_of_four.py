#342. Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or (n & (n - 1)) != 0:
            return False
        return (n & 0x55555555) != 0
 
#Time complexity : O(1)
#Space complexity : O(1)