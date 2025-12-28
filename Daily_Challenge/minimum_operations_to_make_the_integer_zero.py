#2749. Minimum Operations to Make the Integer Zero

import math

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            target = num1 - k * num2
            
            # Condition 1: target must be at least k
            if target < k:
                return -1

            # Condition 2: popcount(target) must be <= k
            popcount = 0
            temp_target = target
            while temp_target > 0:
                popcount += (temp_target & 1)
                temp_target >>= 1
            
            if popcount <= k:
                return k
        
        return -1

#Time complexity: O(log n)
#Space complexity: O(1)
#Where n is the value of num1.