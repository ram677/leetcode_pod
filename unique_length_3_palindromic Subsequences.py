#1930. Unique Length-3 Palindromic Subsequences

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Get all unique characters present in the string to use as potential "bookends"
        unique_chars = set(s)
        total_palindromes = 0
        
        for char in unique_chars:
            # Find the very first and very last occurrence of this character
            first_index = s.find(char)
            last_index = s.rfind(char)
            
            # If there is space between the first and last occurrence
            if last_index > first_index + 1:
                # Get all characters strictly between the two occurrences
                middle_substring = s[first_index + 1 : last_index]
                
                # The number of unique characters in the middle is the number
                # of unique palindromes we can form with 'char' as the outer edges.
                total_palindromes += len(set(middle_substring))
                
        return total_palindromes
    
# Time Complexity: O(n * m) where n is the length of the string and m is the number of unique characters.
# Space Complexity: O(m) for storing unique characters in the middle substrings.