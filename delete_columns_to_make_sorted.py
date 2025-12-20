#944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Number of rows (strings)
        num_rows = len(strs)
        # Number of columns (length of each string)
        num_cols = len(strs[0])
        
        delete_count = 0
        
        # Iterate over each column index
        for col in range(num_cols):
            # Check if this column is sorted top-to-bottom
            for row in range(1, num_rows):
                # Compare current row's char with previous row's char in the same column
                if strs[row][col] < strs[row - 1][col]:
                    delete_count += 1
                    break # Column is bad, move to the next column
                    
        return delete_count
    
# Time Complexity: O(N * M) where N is the number of strings and M is the length of each string.
# Space Complexity: O(1) since we are using only a constant amount of extra space.