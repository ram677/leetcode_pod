#2573. Find the String with LCP

from typing import List
from string import ascii_lowercase

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        """
        Constructs a string from its LCP (Longest Common Prefix) matrix.
      
        Args:
            lcp: A 2D matrix where lcp[i][j] represents the longest common prefix
                 length starting from positions i and j in the target string.
      
        Returns:
            The lexicographically smallest string that matches the LCP matrix,
            or empty string if no valid string exists.
        """
        n = len(lcp)
      
        # Initialize result string array with empty strings
        result_string = [""] * n
      
        # Greedy assignment: assign smallest available character to unassigned positions
        current_position = 0
        for character in ascii_lowercase:
            # Find next unassigned position
            while current_position < n and result_string[current_position]:
                current_position += 1
          
            # All positions have been assigned
            if current_position == n:
                break
          
            # Assign current character to all positions that must have same character
            # based on LCP matrix (if lcp[i][j] > 0, positions i and j must share prefix)
            for j in range(current_position, n):
                if lcp[current_position][j] > 0:
                    result_string[j] = character
      
        # Check if all positions have been assigned
        if "" in result_string:
            return ""
      
        # Validate the constructed string against the LCP matrix
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if result_string[i] == result_string[j]:
                    # Characters match, so LCP should continue
                    if i == n - 1 or j == n - 1:
                        # At boundary: LCP should be exactly 1
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        # Not at boundary: LCP should be 1 + LCP of next positions
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
                else:
                    # Characters don't match, so LCP should be 0
                    if lcp[i][j] != 0:
                        return ""
      
        # Join the character array into final string
        return "".join(result_string)

# Time Complexity: O(n^2) where n is the length of the string, since we need to validate the constructed string against the LCP matrix.
# Space Complexity: O(n) for the result string array, where n is the length of the string.