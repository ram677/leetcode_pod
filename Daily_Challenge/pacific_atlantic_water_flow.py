#417. Pacific Atlantic Water Flow

import collections
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Finds all grid cells from which water can flow to both the Pacific and Atlantic oceans.
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Helper function to perform BFS from a given set of border cells
        def bfs(border_cells: set[tuple[int, int]]) -> set[tuple[int, int]]:
            queue = collections.deque(border_cells)
            reachable = set(border_cells)
            
            while queue:
                r, c = queue.popleft()
                
                # Explore 4-directional neighbors
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    # Check if the neighbor is valid and can "flow" uphill
                    if 0 <= nr < m and 0 <= nc < n and \
                       (nr, nc) not in reachable and \
                       heights[nr][nc] >= heights[r][c]:
                        reachable.add((nr, nc))
                        queue.append((nr, nc))
            return reachable

        # Define the border cells for each ocean
        pacific_border = {(r, 0) for r in range(m)} | {(0, c) for c in range(n)}
        atlantic_border = {(r, n - 1) for r in range(m)} | {(m - 1, c) for c in range(n)}

        # Run BFS from each ocean's border to find all reachable cells
        pacific_reachable = bfs(pacific_border)
        atlantic_reachable = bfs(atlantic_border)
        
        # The result is the intersection of cells reachable from both oceans
        intersection = pacific_reachable.intersection(atlantic_reachable)
        return [list(coord) for coord in intersection]
    
# Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the heights matrix.
# Space Complexity: O(m * n) in the worst case for the BFS queue and reachable sets.