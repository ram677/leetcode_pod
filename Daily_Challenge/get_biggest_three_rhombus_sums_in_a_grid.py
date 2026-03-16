#1878. Get Biggest Three Rhombus Sums in a Grid

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # Use a set to automatically handle distinct sums
        sums = set()
        
        # Iterate through every cell to treat it as the top vertex of a potential rhombus
        for i in range(m):
            for j in range(n):
                # An area 0 rhombus is just the cell itself
                sums.add(grid[i][j])
                
                # Expand the side length (L) of the rhombus
                L = 1
                
                # Check if a rhombus of side length L starting at (i, j) fits in the grid.
                # The bottom tip will be at i + 2*L.
                # The left tip will be at j - L, and the right tip at j + L.
                while i + 2 * L < m and j - L >= 0 and j + L < n:
                    curr = 0
                    x, y = i, j
                    
                    # Trace the 4 sides of the rhombus, adding the cell values
                    
                    # 1. Move down-right
                    for _ in range(L):
                        x += 1
                        y += 1
                        curr += grid[x][y]
                        
                    # 2. Move down-left
                    for _ in range(L):
                        x += 1
                        y -= 1
                        curr += grid[x][y]
                        
                    # 3. Move up-left
                    for _ in range(L):
                        x -= 1
                        y -= 1
                        curr += grid[x][y]
                        
                    # 4. Move up-right (back to the starting top vertex)
                    for _ in range(L):
                        x -= 1
                        y += 1
                        curr += grid[x][y]
                        
                    # Add the perimeter sum to our set
                    sums.add(curr)
                    
                    # Increase the side length to check larger rhombuses from this top vertex
                    L += 1
                    
        # Sort the unique sums in descending order and return up to the top 3
        return sorted(list(sums), reverse=True)[:3]
    
# Time Complexity: O(m * n * L) where L is the maximum side length of the rhombus that can fit in the grid. In the worst case, L can be O(min(m, n)), where m and n are the dimensions of the grid. Thus, the overall time complexity can be O(m * n * min(m, n)).
# Space Complexity: O(k) where k is the number of distinct rhombus sums, which can be at most O(m * n) in the worst case.