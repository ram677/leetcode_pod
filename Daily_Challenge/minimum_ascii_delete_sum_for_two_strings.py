#712. Minimum ASCII Delete Sum for Two Strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Find the minimum ASCII sum of deleted characters to make two strings equal.
      
        Args:
            s1: First input string
            s2: Second input string
          
        Returns:
            Minimum sum of ASCII values of deleted characters
        """
        # Get lengths of both strings
        len_s1, len_s2 = len(s1), len(s2)
      
        # Create DP table where dp[i][j] represents the minimum delete sum
        # for s1[0:i] and s2[0:j] to make them equal
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
      
        # Initialize first column: delete all characters from s1[0:i]
        for i in range(1, len_s1 + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
      
        # Initialize first row: delete all characters from s2[0:j]
        for j in range(1, len_s2 + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
      
        # Fill the DP table
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match: no deletion needed for these characters
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Characters don't match: delete from either s1 or s2
                    # Choose the option with minimum ASCII sum
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),  # Delete from s1
                        dp[i][j - 1] + ord(s2[j - 1])   # Delete from s2
                    )
      
        # Return the minimum delete sum for entire strings
        return dp[len_s1][len_s2]

# Time Complexity: O(m * n), where m and n are lengths of s1 and s2.
# Space Complexity: O(m * n) for the DP table.