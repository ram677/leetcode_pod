#2197. Replace Non-Coprime Numbers in Array

import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # The result list 'res' will be used as a stack.
        res = []
        
        for num in nums:
            current_num = num
            
            # While the stack is not empty and the top element is non-coprime
            # with the current number, merge them.
            while res and math.gcd(res[-1], current_num) > 1:
                # Pop the last element to merge it.
                last_element = res.pop()
                
                # Calculate the LCM and update the current number.
                # LCM(a, b) = (a * b) // GCD(a, b)
                current_num = (last_element * current_num) // math.gcd(last_element, current_num)
            
            # After all possible merges, add the resulting number to the stack.
            res.append(current_num)
            
        return res
    
# Time Complexity: O(n * log(max(nums))), where n is the length of nums and max(nums) is the maximum number in nums.
# Space Complexity: O(n) in the worst case, where all numbers are coprime and we store them all in the result list.