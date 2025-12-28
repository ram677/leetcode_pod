#778. Swim in Rising Water

import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Priority queue stores tuples of (time, row, col).
        # 'time' is the maximum elevation encountered on the path to (row, col).
        pq = [(grid[0][0], 0, 0)]
        
        # A set to keep track of visited cells to prevent cycles.
        visited = set([(0, 0)])
        
        while pq:
            # Get the cell that can be reached with the minimum water level so far.
            time, r, c = heapq.heappop(pq)
            
            # If we've reached the bottom-right corner, we're done.
            # This is the minimum possible time due to the nature of the min-heap.
            if r == n - 1 and c == n - 1:
                return time
            
            # Explore the 4-directional neighbors.
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # Check if the neighbor is within the grid and hasn't been visited.
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # The time to reach this neighbor is the maximum of the current path's
                    # required time and the neighbor's own elevation.
                    new_time = max(time, grid[nr][nc])
                    
                    heapq.heappush(pq, (new_time, nr, nc))

# Time Complexity: O(n^2 log(n^2)) = O(n^2 log n) where n is the dimension of the grid.
# Space Complexity: O(n^2) for the priority queue and visited set in the worst case.