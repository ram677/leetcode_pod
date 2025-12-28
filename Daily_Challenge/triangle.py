#120. Triangle

from typing import List

class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # Get the number of rows in the triangle.
    n = len(triangle)
    
    # We start from the second-to-last row and move upwards.
    # The range goes from n-2 down to 0.
    for i in range(n - 2, -1, -1):
      # For each element in the current row...
      for j in range(len(triangle[i])):
        # ...update its value to be the minimum path sum starting from this cell.
        # This is the cell's value plus the minimum of its two children in the row below.
        min_child_path = min(triangle[i + 1][j], triangle[i + 1][j + 1])
        triangle[i][j] += min_child_path
        
    # By the end of the loops, the top element of the triangle (triangle[0][0])
    # will hold the overall minimum path sum from top to bottom.
    return triangle[0][0]
  
# Time Complexity: O(n^2) where n is the number of rows in the triangle.
# Space Complexity: O(1) since we are modifying the triangle in place.