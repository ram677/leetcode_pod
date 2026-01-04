#1390. Four Divisors

import math
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        
        for num in nums:
            divisors = set()
            # Iterate only up to the square root of num
            for i in range(1, int(math.isqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)
                    
                    # Optimization: If we already have more than 4 divisors, stop.
                    if len(divisors) > 4:
                        break
            
            if len(divisors) == 4:
                total_sum += sum(divisors)
                
        return total_sum
    
# Time Complexity: O(m * sqrt(k)), where m is the number of elements in nums and k is the maximum value in nums.
# Space Complexity: O(1).