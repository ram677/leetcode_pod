#1015. Smallest Integer Divisible by K

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Optimization: Multiples of 2 and 5 can never end in '1'
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        
        # We iterate length from 1 up to k.
        # By Pigeonhole Principle, if we don't find a remainder of 0 
        # within k iterations, we are in a loop that doesn't include 0.
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
                
        return -1

# Time Complexity: O(k) in the worst case, where k is the input integer.
# Space Complexity: O(1) as we use a constant amount of space.