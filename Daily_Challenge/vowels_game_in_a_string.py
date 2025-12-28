#3227. Vowels Game in a String

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        vowel_count = 0
        for char in s:
            if char in vowels:
                vowel_count += 1
                
        # If there is at least one vowel, Alice can always make a move.
        # For example, by taking a substring of length 1 containing a single vowel.
        # This forces a state where she can eventually win.
        # If there are no vowels, she cannot make a move.
        return vowel_count > 0
    
#Time Complexity: O(n), where n is the length of the string.
#Space Complexity: O(1)