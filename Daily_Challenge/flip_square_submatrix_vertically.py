#3643. Flip Square Submatrix Vertically

class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        """
        Reverses rows within a k×k submatrix starting at position (x, y).
        The submatrix rows are flipped vertically (top rows swap with bottom rows).
      
        Args:
            grid: 2D list representing the matrix
            x: Starting row index of the submatrix
            y: Starting column index of the submatrix
            k: Size of the square submatrix (k×k)
      
        Returns:
            Modified grid with reversed submatrix rows
        """
        # Iterate through the first half of the submatrix rows
        for row_idx in range(x, x + k // 2):
            # Calculate the corresponding row index from the bottom
            # that should be swapped with the current row
            mirror_row_idx = x + k - 1 - (row_idx - x)
          
            # Swap all elements in the current row with the mirror row
            # within the column range [y, y + k)
            for col_idx in range(y, y + k):
                grid[row_idx][col_idx], grid[mirror_row_idx][col_idx] = (
                    grid[mirror_row_idx][col_idx], 
                    grid[row_idx][col_idx]
                )
      
        return grid
    
# Time Complexity: O(k^2) for flipping the submatrix, where k is the size of the submatrix.
# Space Complexity: O(1) since the operation is done in-place without using extra space.