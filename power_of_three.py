#326. Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1

#Time Complexity: O(log n)
#Space Complexity: O(1)
#where n is the input integer.