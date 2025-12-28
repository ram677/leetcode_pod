#3195. Find the Minimum Area to Cover All Ones I

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        min_row, max_row = rows, -1
        min_col, max_col = cols, -1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        # Area = height * width
        return (max_row - min_row + 1) * (max_col - min_col + 1)

#Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid.
#Space Complexity: O(1), as we are using only a constant amount of extra space.