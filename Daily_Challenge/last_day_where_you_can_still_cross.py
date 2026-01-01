#1970. Last Day Where You Can Still Cross

from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if self.canCross(row, col, mid, cells):
                ans = mid      # If possible, store this day as a potential answer
                left = mid + 1 # Try to find a later day
            else:
                right = mid - 1 # If not possible, look for an earlier day
        
        return ans

    def canCross(self, row, col, day, cells):
        grid = [[0] * col for _ in range(row)]
        
        # Mark the cells that turn into water up to the current 'day'
        # Note: Input cells are 1-based, grid is 0-based
        for i in range(day):
            r, c = cells[i]
            grid[r-1][c-1] = 1  # 1 represents water
            
        queue = deque()
        
        # Add all starting land cells (top row) to the queue
        for c in range(col):
            if grid[0][c] == 0: # If it's land
                queue.append((0, c))
                grid[0][c] = 1  # Mark as visited to avoid cycles
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            # If we reached the bottom row, a path exists
            if r == row - 1:
                return True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and if the neighbor is land (0)
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = 1 # Mark as visited
                    queue.append((nr, nc))
                    
        return False
    
# Time Complexity: O(row * col * log(row * col)), where row and col are the dimensions of the grid.
# Space Complexity: O(row * col) for the grid and the queue used in BFS.