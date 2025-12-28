#1578. Minimum Time to Make Rope Colorful

from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        total_time_cost = 0
        
        # 'max_time_in_group' holds the time of the balloon we've decided
        # to keep so far in the current consecutive group.
        max_time_in_group = 0
        
        for i in range(len(colors)):
            # Check if this balloon is part of the previous group.
            if i > 0 and colors[i] == colors[i-1]:
                # We have two consecutive balloons of the same color.
                # We must remove one. We remove the cheaper one.
                # 'max_time_in_group' is the cost of the one we kept from the
                # previous comparison.
                
                # Add the cost of the cheaper balloon to our total.
                total_time_cost += min(max_time_in_group, neededTime[i])
                
                # Update the 'max_time_in_group' to be the one we are keeping
                # for the next comparison.
                max_time_in_group = max(max_time_in_group, neededTime[i])
            else:
                # This is a new color, so we just set the max time for this
                # (new) group.
                max_time_in_group = neededTime[i]
                
        return total_time_cost
    
# Time Complexity: O(n), where n is the length of the colors string.
# Space Complexity: O(1), we use a constant amount of extra space.