#1415. The k-th Lexicographical String of All Happy Strings of Length n

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total number of happy strings of length n is 3 * 2^(n-1)
        total_happy = 3 * (1 << (n - 1))
        
        # If k is out of bounds, return an empty string
        if k > total_happy:
            return ""
            
        # Convert k to 0-indexed for easier math
        k -= 1
        res = []
        chars = ['a', 'b', 'c']
        
        # Determine the first character
        # The block size for the first character choices is 2^(n-1)
        group_size = 1 << (n - 1)
        first_char_idx = k // group_size
        res.append(chars[first_char_idx])
        k %= group_size
        
        # Determine the subsequent characters
        for i in range(n - 1, 0, -1):
            # The block size halves for each subsequent position
            group_size = 1 << (i - 1)
            
            # The available choices are the two characters not equal to the last placed one
            # Because 'chars' is sorted, this maintains the lexicographical order naturally
            next_chars = [c for c in chars if c != res[-1]]
            
            next_char_idx = k // group_size
            res.append(next_chars[next_char_idx])
            k %= group_size
            
        return "".join(res)
    
# Time Complexity: O(n), where n is the length of the happy string. We determine each character in a single pass.
# Space Complexity: O(n), as we are storing the resulting happy string in a list before joining it into a final string.