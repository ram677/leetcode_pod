#2257. Count Unguarded Cells in the Grid

from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        # Initialize the grid
        grid = [[0 for _ in range(n)] for _ in range(m)]

        # Step 1: Place walls and guards
        for r, c in walls:
            grid[r][c] = 2
        for r, c in guards:
            grid[r][c] = 3

        # Step 2: Scan in all four directions
        
        # Left-to-Right
        for r in range(m):
            guarded_streak = False
            for c in range(n):
                if grid[r][c] == 2:    # Wall
                    guarded_streak = False
                elif grid[r][c] == 3:  # Guard
                    guarded_streak = True
                elif grid[r][c] == 0 and guarded_streak:
                    grid[r][c] = 1 # Mark as guarded

        # Right-to-Left
        for r in range(m):
            guarded_streak = False
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 2:
                    guarded_streak = False
                elif grid[r][c] == 3:
                    guarded_streak = True
                elif grid[r][c] == 0 and guarded_streak:
                    grid[r][c] = 1

        # Top-to-Bottom
        for c in range(n):
            guarded_streak = False
            for r in range(m):
                if grid[r][c] == 2:
                    guarded_streak = False
                elif grid[r][c] == 3:
                    guarded_streak = True
                elif grid[r][c] == 0 and guarded_streak:
                    grid[r][c] = 1

        # Bottom-to-Top
        for c in range(n):
            guarded_streak = False
            for r in range(m - 1, -1, -1):
                if grid[r][c] == 2:
                    guarded_streak = False
                elif grid[r][c] == 3:
                    guarded_streak = True
                elif grid[r][c] == 0 and guarded_streak:
                    grid[r][c] = 1
        
        # Step 3: Count unguarded cells
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count += 1
        
        return count
    
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m * n) for the grid storage.