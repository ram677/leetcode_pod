#1351. Count Negative Numbers in a Sorted Matrix

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        # Start from the bottom-left corner
        row = m - 1
        col = 0
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # If current number is negative, all numbers to its right 
                # in this row are also negative (since row is non-increasing).
                # Add all remaining columns in this row to count.
                count += (n - col)
                
                # Move up to check if the row above has negatives
                row -= 1
            else:
                # If current is positive, move right to find smaller numbers
                col += 1
                
        return count
    
# Time Complexity: O(m + n), where m is the number of rows and n is the number of columns.
# Space Complexity: O(1).