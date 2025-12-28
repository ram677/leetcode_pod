#3027. Find the Number of Ways to Place People II

import math
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        # Sort points: x-coordinate ascending, y-coordinate descending for ties.
        points.sort(key=lambda p: (p[0], -p[1]))
        
        n = len(points)
        count = 0
        
        # Iterate through each point, considering it as Alice.
        for i in range(n):
            alice_y = points[i][1]
            
            # For a fixed Alice, this tracks the maximum y-coordinate of any
            # Bob candidate found so far.
            max_y_of_candidates = -math.inf
            
            # Iterate through subsequent points to consider them as Bob.
            for j in range(i + 1, n):
                bob_y = points[j][1]
                
                # Check if the point is a candidate for Bob (in Alice's lower-right quadrant).
                if bob_y <= alice_y:
                    # To be a valid pair, this candidate Bob cannot be dominated by any
                    # previous candidate. This is true if its y-coordinate is greater
                    # than the maximum y seen among previous candidates.
                    if bob_y > max_y_of_candidates:
                        count += 1
                    
                    # Update the max y seen so far among candidates for this Alice.
                    max_y_of_candidates = max(max_y_of_candidates, bob_y)
            
        return count

#Time Complexity: O(n^2)
#Space Complexity: O(1)
#Where n is the number of points in the input list.