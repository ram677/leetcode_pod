#3625. Count Number of Trapezoids II

import math
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        
        # Data structures to group segments
        # slope_map: (dx_reduced, dy_reduced) -> { (A, B, C) -> count }
        slope_map = defaultdict(lambda: defaultdict(int))
        
        # vector_map: (dx_raw, dy_raw) -> { (A, B, C) -> count }
        vector_map = defaultdict(lambda: defaultdict(int))
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                # 1. Slope Key (Reduced by GCD)
                g = math.gcd(dx, dy)
                sdx, sdy = dx // g, dy // g
                
                # Normalize slope direction (force first non-zero to be positive)
                if sdx < 0 or (sdx == 0 and sdy < 0):
                    sdx, sdy = -sdx, -sdy
                slope_key = (sdx, sdy)
                
                # 2. Line Key (Equation Ax + By + C = 0)
                # Slope is dy/dx, so line is sdy*x - sdx*y + C = 0
                # A = sdy, B = -sdx
                # We need C.  sdy*x1 - sdx*y1 + C = 0  => C = -sdy*x1 + sdx*y1
                A = sdy
                B = -sdx
                C = -A * x1 - B * y1
                line_key = (A, B, C)
                
                # Add to slope map
                slope_map[slope_key][line_key] += 1
                
                # 3. Vector Key (Raw dx, dy)
                # Normalize vector to treat AB and BA as same segment vector
                vdx, vdy = dx, dy
                if vdx < 0 or (vdx == 0 and vdy < 0):
                    vdx, vdy = -vdx, -vdy
                vector_key = (vdx, vdy)
                
                # Add to vector map
                vector_map[vector_key][line_key] += 1
                
        # Calculate Raw Trapezoid Count
        raw_trapezoid_count = 0
        for slope in slope_map:
            # Get counts of segments for each distinct line with this slope
            counts = list(slope_map[slope].values())
            
            # We need to choose 2 segments from DIFFERENT lines.
            # Sum of products of all pairs: sum(count[i] * count[j]) for i < j
            # Identity: 2 * sum(a*b) = (sum(a))^2 - sum(a^2)
            
            sum_counts = sum(counts)
            sum_sq_counts = sum(c * c for c in counts)
            
            pairs = (sum_counts * sum_counts - sum_sq_counts) // 2
            raw_trapezoid_count += pairs
            
        # Calculate Parallelogram Hits
        parallelogram_hits = 0
        for vec in vector_map:
            counts = list(vector_map[vec].values())
            
            # Similar calculation: choose 2 segments with same vector from DIFFERENT lines
            sum_counts = sum(counts)
            sum_sq_counts = sum(c * c for c in counts)
            
            pairs = (sum_counts * sum_counts - sum_sq_counts) // 2
            parallelogram_hits += pairs
            
        # Final Result
        # Each parallelogram is counted twice in 'raw_trapezoid_count' (once for each pair of parallel sides).
        # We want to count it exactly once.
        # 'parallelogram_hits' counts the number of times we found parallel EQUAL vectors.
        # For a parallelogram, we will find a hit for the first pair of sides, and a hit for the second pair.
        # So 'parallelogram_hits' is exactly 2 * number_of_parallelograms.
        # Therefore, we subtract (parallelogram_hits // 2).
        
        return raw_trapezoid_count - (parallelogram_hits // 2)
    
# Time Complexity: O(n^2), where n is the number of points.
# Space Complexity: O(n^2), for storing slopes and vectors.