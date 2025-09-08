#1317. Convert Integer to the Sum of Two No-Zero Integers

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def is_no_zero(num):
            return '0' not in str(num)

        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the input integer.