#3025. Find the Number of Ways to Place People I

from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        n = len(points)
        
        # Sort points by x-coordinate ascending, then y-coordinate descending.
        # This ensures that for any i < j, points[i][0] <= points[j][0].
        points.sort(key=lambda p: (p[0], -p[1]))
        
        count = 0
        
        # Iterate through all possible pairs (A, B) where A comes before B in the sorted list.
        for i in range(n):
            # A is points[i]
            y_a = points[i][1]
            
            for j in range(i + 1, n):
                # B is points[j]
                y_b = points[j][1]
                
                # Check if A is upper-left of B.
                # A.x <= B.x is guaranteed by the sort. We just need to check the y-coordinates.
                if y_a >= y_b:
                    
                    # This is a potential valid pair. Now, check that no other point
                    # lies inside the rectangle defined by A and B.
                    
                    is_valid_pair = True
                    
                    # Any obstructing point C=points[k] must have an index k such that i < k < j.
                    # For such a point C, we already know A.x <= C.x <= B.x.
                    # We only need to check its y-coordinate.
                    for k in range(i + 1, j):
                        y_c = points[k][1]
                        
                        # Check if C is vertically between B and A (inclusive).
                        if y_b <= y_c <= y_a:
                            # This point C invalidates the pair (A, B).
                            is_valid_pair = False
                            break
                    
                    if is_valid_pair:
                        count += 1
                        
        return count

#Time Complexity: O(n^3)
#Space Complexity: O(1)
#Where n is the number of points in the input list.