#757. Set Intersection Size At Least Two

from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end time ascending. 
        # If end times are equal, sort by start time descending.
        # This ensures we process the "hardest" constraint first for same-end intervals.
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        count = 0
        
        # p1 is the second largest number added to the set
        # p2 is the largest number added to the set
        p1 = -1
        p2 = -1
        
        for s, e in intervals:
            # Check how many of our current "best" numbers fall in this interval
            
            # Case 1: Neither p1 nor p2 are in [s, e]
            # We need to add two numbers. Greedily pick the last two.
            if s > p2:
                count += 2
                p1 = e - 1
                p2 = e
            
            # Case 2: Only p2 is in [s, e] (p1 is outside)
            # We need one more number. Greedily pick the last one.
            elif s > p1:
                count += 1
                p1 = p2  # The old max becomes the new second max
                p2 = e   # The current end becomes the new max
            
            # Case 3: Both p1 and p2 are in [s, e]
            # We are already good (since s <= p1 < p2 <= e).
            
        return count
    
# Time Complexity: O(n log n) due to sorting the intervals.
# Space Complexity: O(1) if we ignore the space used for sorting.