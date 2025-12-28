#1925. Count Square Sum Triples

import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        
        # Iterate through all pairs (a, b)
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # Calculate potential c^2
                target = a * a + b * b
                
                # Calculate integer square root
                c = int(math.isqrt(target))
                
                # Check if it's a perfect square and within range
                if c * c == target and c <= n:
                    count += 1
                    
        return count
    
# Time Complexity: O(n^2), where n is the input number.
# Space Complexity: O(1)