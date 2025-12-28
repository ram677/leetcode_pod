#955. Delete Columns to Make Sorted II

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # is_sorted[i] tracks if strs[i] < strs[i+1] is already satisfied
        is_sorted = [False] * (n - 1)
        delete_count = 0
        
        for col in range(m):
            must_delete = False
            
            # Check if this column causes a violation
            for i in range(n - 1):
                # We only care about pairs that are NOT yet strictly sorted
                if not is_sorted[i] and strs[i][col] > strs[i+1][col]:
                    must_delete = True
                    break
            
            if must_delete:
                # If even one pair violates order, we must delete this column
                delete_count += 1
            else:
                # Keep the column and update sorted status for rows
                for i in range(n - 1):
                    if not is_sorted[i] and strs[i][col] < strs[i+1][col]:
                        is_sorted[i] = True
                        
        return delete_count

# Time Complexity: O(n * m), where n is the number of strings and m is the length of each string.
# Space Complexity: O(n) for the is_sorted array.