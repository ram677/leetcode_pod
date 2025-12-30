#840. Magic Squares In Grid

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        # Helper function to check if a 3x3 grid starting at (r, c) is a magic square
        def isMagic(r, c):
            # 1. Check distinct numbers 1-9
            # We can use a set or sorted list. 
            # Since the grid is small, extracting elements is cheap.
            vals = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    val = grid[i][j]
                    # Optimization: Fail early if value is out of range
                    if val < 1 or val > 9:
                        return False
                    vals.append(val)
            
            if len(set(vals)) != 9:
                return False
                
            # 2. Check Sums (Target is 15)
            # Rows
            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
                return False
            
            # Columns
            if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
                return False
                
            # Diagonals
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False
                
            return True

        # Iterate over all possible top-left corners of 3x3 subgrids
        for r in range(rows - 2):
            for c in range(cols - 2):
                # Optimization: The center of a 1-9 magic square must be 5
                if grid[r+1][c+1] != 5:
                    continue
                
                if isMagic(r, c):
                    count += 1
                    
        return count
    
# Time Complexity: O(m * n) where m and n are the dimensions of the grid.
# Space Complexity: O(1).