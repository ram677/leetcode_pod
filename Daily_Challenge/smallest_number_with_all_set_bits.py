#3370. Smallest Number With All Set Bits

class Solution:
    def smallestNumber(self, n: int) -> int:
        # Start with the first number in the sequence (binary '1').
        x = 1
        
        # Keep generating the next number in the sequence (1, 3, 7, 15, ...)
        # until our candidate is no longer smaller than n.
        while x < n:
            # Generate the next number by shifting left and adding 1.
            # e.g., 7 (111) -> 14 (1110) -> 15 (1111)
            x = (x << 1) + 1
            
        # The loop stops when x >= n, which is our answer.
        return x