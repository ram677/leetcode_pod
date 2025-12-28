#3541. Find Most Frequent Vowel and Consonant

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_freq = {}
        consonant_freq = {}
        
        for char in s:
            if char in vowels:
                vowel_freq[char] = vowel_freq.get(char, 0) + 1
            else:
                consonant_freq[char] = consonant_freq.get(char, 0) + 1
        
        max_vowel_freq = 0
        if vowel_freq:
            max_vowel_freq = max(vowel_freq.values())
            
        max_consonant_freq = 0
        if consonant_freq:
            max_consonant_freq = max(consonant_freq.values())
            
        return max_vowel_freq + max_consonant_freq
    
#Time Complexity: O(n), where n is the length of the string.
#Space Complexity: O(1) since the size of the frequency dictionaries is bounded by the number of letters in the alphabet (26).