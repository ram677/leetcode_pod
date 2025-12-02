#3623. Count Number of Trapezoids I

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # 1. Group x-coordinates by their y-coordinate
        y_map = {}
        for x, y in points:
            if y not in y_map:
                y_map[y] = 0
            y_map[y] += 1
            
        # 2. Calculate number of horizontal segments at each level
        # A level with 'n' points can form nC2 segments.
        segment_counts = []
        for y in y_map:
            n = y_map[y]
            if n >= 2:
                count = (n * (n - 1)) // 2
                segment_counts.append(count)
        
        if len(segment_counts) < 2:
            return 0
            
        # 3. Calculate sum of products of all pairs
        # Result = Sum(count[i] * count[j]) for all i < j
        # We use the formula: sum_products = ( (sum)^2 - sum_squares ) // 2
        
        total_sum = sum(segment_counts)
        sum_sq = sum(c * c for c in segment_counts)
        
        # Calculate in standard integer arithmetic first, then mod at the end
        # or handle mod carefully. Python handles large integers automatically, 
        # so we can compute the exact value and then mod.
        
        result = (total_sum * total_sum - sum_sq) // 2
        
        return result % MOD
    
# Time Complexity: O(m), where m is the number of points.
# Space Complexity: O(m), for storing the y_map and segment counts.