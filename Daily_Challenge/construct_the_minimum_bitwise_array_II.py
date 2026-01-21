#3315. Construct the Minimum Bitwise Array II

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                # n is prime and > 2, so it is odd.
                # n looks like ...011...1 in binary.
                # n ^ (n + 1) creates a mask of all trailing ones plus the first zero flipped.
                # Example: n = 11 (1011), n+1 = 12 (1100), xor = 7 (0111)
                t = n ^ (n + 1)
                
                # t is of the form 2^(c+1) - 1.
                # We want to subtract the bit corresponding to the highest trailing 1, which is 2^(c-1).
                # (t + 1) is 2^(c+1).
                # (t + 1) >> 2 is 2^(c-1).
                bit_to_remove = (t + 1) >> 2
                
                ans.append(n - bit_to_remove)
                
        return ans
    
# Time complexity: O(n), where n is the length of nums.
# Space complexity: O(1) excluding the output array.