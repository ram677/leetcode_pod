#3446. Sort Matrix by Diagonals

from typing import List
from collections import defaultdict

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        # 1. Use a dictionary to store elements of each diagonal.
        # The key (i - j) is constant for any given diagonal.
        diagonals = defaultdict(list)
        for i in range(n):
            for j in range(n):
                diagonals[i - j].append(grid[i][j])
        
        # 2. Sort each diagonal based on its key.
        for key in diagonals:
            if key >= 0:
                # Bottom-left and main diagonals: sort non-increasingly (descending)
                diagonals[key].sort(reverse=True)
            else:
                # Top-right diagonals: sort non-decreasingly (ascending)
                diagonals[key].sort()
                
        # 3. Place the sorted elements back into the grid.
        for i in range(n):
            for j in range(n):
                # The first element in the sorted list corresponds to the
                # first cell of that diagonal we encounter.
                grid[i][j] = diagonals[i - j].pop(0)
                
        return grid

#Time Complexity: O(N^2 log N), where N is the number of rows (or columns) in the grid.
#Space Complexity: O(N^2), for storing the diagonal elements.