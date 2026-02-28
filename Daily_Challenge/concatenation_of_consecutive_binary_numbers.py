#1680. Concatenation of Consecutive Binary Numbers

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        
        for i in range(1, n + 1):
            result = ((result << i.bit_length()) | i) % MOD
            
        return result
    
# Time Complexity: O(n), where n is the input number, since we iterate through all numbers from 1 to n.
# Space Complexity: O(1), as we use only a constant amount of extra space.