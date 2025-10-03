#407. Trapping Rain Water II

import heapq
from typing import List

class Solution:
  def trapRainWater(self, heightMap: List[List[int]]) -> int:
    if not heightMap or not heightMap[0]:
      return 0
    
    m, n = len(heightMap), len(heightMap[0])
    
    # If the map is too small to trap any water
    if m <= 2 or n <= 2:
      return 0
        
    visited = [[False] * n for _ in range(m)]
    # Min-heap will store tuples of (height, row, col)
    min_heap = []
    
    # Step 1: Add all border cells to the min-heap and mark as visited
    for r in range(m):
      for c in range(n):
        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
          heapq.heappush(min_heap, (heightMap[r][c], r, c))
          visited[r][c] = True
                
    trapped_water = 0
    
    # Step 2 & 3: Process cells from the lowest boundary point inwards
    while min_heap:
      # The height of the popped element is the current water level
      height, r, c = heapq.heappop(min_heap)
      
      # Explore the four neighbors
      for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        
        # Check if the neighbor is within bounds and has not been visited
        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
          visited[nr][nc] = True
          
          # If the neighbor is lower than the current water level, it traps water
          if heightMap[nr][nc] < height:
            trapped_water += height - heightMap[nr][nc]
          
          # Add the neighbor to the heap (our new boundary).
          # Its effective height is the maximum of its own height and the current water level.
          new_height = max(height, heightMap[nr][nc])
          heapq.heappush(min_heap, (new_height, nr, nc))
                
    return trapped_water
  
# Time Complexity: O(m * n * log(m + n)) where m and n are the dimensions of the heightMap.
# This is because each cell is processed once and added to the heap, and heap operations take O(log(m + n)) time.
# Space Complexity: O(m * n) for the visited array and the heap in the worst case.