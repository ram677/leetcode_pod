#1039. Minimum Score Triangulation of Polygon

from typing import List
import math

class Solution:
  def minScoreTriangulation(self, values: List[int]) -> int:
    n = len(values)
    
    # dp[i][j] will store the minimum score to triangulate
    # the polygon with vertices from i to j.
    dp = [[0] * n for _ in range(n)]
    
    # Iterate over the length of the polygon chain.
    # Length is the number of vertices, j - i + 1. We start with length 3 (a triangle).
    for length in range(3, n + 1):
      # Iterate over the starting vertex i.
      for i in range(n - length + 1):
        # Calculate the ending vertex j.
        j = i + length - 1
        
        # Initialize the score for this subproblem to infinity.
        dp[i][j] = math.inf
        
        # Iterate over the intermediate vertex k to form a triangle (i, k, j).
        # This vertex 'k' splits the polygon (i, ..., j) into two smaller ones:
        # (i, ..., k) and (k, ..., j), whose scores we've already computed.
        for k in range(i + 1, j):
          current_score = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
          dp[i][j] = min(dp[i][j], current_score)
          
    # The final answer is the score for the entire polygon, from vertex 0 to n-1.
    return dp[0][n - 1]
  
# Time Complexity: O(n^3) due to the three nested loops.
# Space Complexity: O(n^2) for the dp table.    
# WHere n is the number of vertices in the polygon.