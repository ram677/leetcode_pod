#1304. Find N Unique Integers Sum up to Zero

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result.append(0)
            
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
            
        return result

#Time Complexity: O(n)
#Space Complexity: O(n) 
#Where n is the input integer.