#3461. Check If Digits Are Equal in String After Operations I

from typing import List

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Keep applying the operation while the string has more than two digits.
        while len(s) > 2:
            next_s = ""
            # Calculate the new string from the sums of adjacent digits.
            for i in range(len(s) - 1):
                digit1 = int(s[i])
                digit2 = int(s[i+1])
                new_digit = (digit1 + digit2) % 10
                next_s += str(new_digit)
            
            # Replace the old string with the new one for the next iteration.
            s = next_s
        
        # After the loop, the string has exactly two digits. Check if they are equal.
        return s[0] == s[1]
    
#Time Complexity: O(n^2) in the worst case, where n is the length of the string.
#Space Complexity: O(n) for storing the intermediate strings.