#3713. Longest Balanced Substring I

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Iterate over all possible starting positions
        for i in range(n):
            counts = {}
            max_freq = 0
            
            # Extend the substring to the right
            for j in range(i, n):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                
                # Keep track of the highest frequency in the current window
                max_freq = max(max_freq, counts[char])
                
                # Current length of substring s[i...j]
                current_len = j - i + 1
                
                # Check if balanced: 
                # If valid, total length must equal (number of unique chars) * (frequency of each)
                # Since we know the max frequency, we check if max_freq * unique_count == total_length
                if max_freq * len(counts) == current_len:
                    max_len = max(max_len, current_len)
                    
        return max_len
    
# Time Complexity: O(n^2) due to the nested loops, where n is the length of the string. 
# Space Complexity: O(k) where k is the number of unique characters in the substring, which is at most 26 for lowercase letters.