#960. Delete Columns to Make Sorted III

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        # dp[i] stores the max length of an increasing subsequence of columns ending at column i
        # Initialize with 1 because each column alone is a valid subsequence of length 1
        dp = [1] * m
        
        # Iterate through every column 'i'
        for i in range(m):
            # Check all previous columns 'j'
            for j in range(i):
                # Check if column 'i' can extend the subsequence ending at column 'j'
                # It is valid only if for EVERY string (row), the char at j is <= char at i
                valid = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        valid = False
                        break
                
                # If valid, we update dp[i]
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The result is the total columns minus the max columns we can keep
        max_kept = max(dp) if m > 0 else 0
        return m - max_kept

# Time Complexity: O(n * m^2) where n is the number of strings and m is the length of each string.
# Space Complexity: O(m) for the dp array.