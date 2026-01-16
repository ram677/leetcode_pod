#2975. Maximum Square Area by Removing Fences From a Field

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Include the boundaries of the field (1 and m/n)
        # We need sorted lists to easily calculate distances between any pair
        h_coords = sorted(hFences + [1, m])
        v_coords = sorted(vFences + [1, n])
        
        # Step 1: Collect all possible heights we can form
        h_gaps = set()
        for i in range(len(h_coords)):
            for j in range(i + 1, len(h_coords)):
                # The distance between any two horizontal fences is a possible side length
                h_gaps.add(h_coords[j] - h_coords[i])
        
        # Step 2: Check all possible widths and look for a match
        max_side = -1
        for i in range(len(v_coords)):
            for j in range(i + 1, len(v_coords)):
                current_gap = v_coords[j] - v_coords[i]
                
                # If this width matches a possible height, we can form a square
                if current_gap in h_gaps:
                    max_side = max(max_side, current_gap)
        
        # Step 3: Return result with modulo
        if max_side == -1:
            return -1
        
        return (max_side * max_side) % (10**9 + 7)
    
# Time Complexity: O(H^2 + V^2) where H is the number of horizontal fences and V is the number of vertical fences.
# Space Complexity: O(H^2) for storing possible heights in the worst case.