#3567. Minimum Absolute Difference in Sliding Submatrix

from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        # Iterate over all possible top-left corners of the k x k submatrix
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                
                # Use a set to store distinct values in the current submatrix
                distinct_vals = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        distinct_vals.add(grid[r][c])
                
                # If there are less than 2 distinct elements, the difference is 0
                if len(distinct_vals) < 2:
                    ans[i][j] = 0
                else:
                    # Sort the distinct values to easily find the minimum difference
                    sorted_vals = sorted(list(distinct_vals))
                    min_diff = float('inf')
                    
                    # The minimum difference between any two numbers in a sorted list
                    # will always be between two adjacent numbers
                    for v1, v2 in zip(sorted_vals, sorted_vals[1:]):
                        if v2 - v1 < min_diff:
                            min_diff = v2 - v1
                            
                    ans[i][j] = min_diff
                    
        return ans
    
# Time Complexity: O(m * n * k^2) where m and n are the dimensions of the grid and k is the size of the submatrix.
# Space Complexity: O(m * n) for the answer array and O(k^2) for the set of distinct values in the worst case.