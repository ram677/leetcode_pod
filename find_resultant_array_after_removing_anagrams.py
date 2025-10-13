#2273. Find Resultant Array After Removing Anagrams

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # If the list is empty or has one word, no operations are possible.
        if len(words) <= 1:
            return words
            
        # The result will always contain the first word.
        result = [words[0]]
        
        # Iterate from the second word to the end of the list.
        for i in range(1, len(words)):
            # Compare the current word with the last word added to our result.
            # Sorting the characters is an easy way to check for anagrams.
            if sorted(words[i]) != sorted(result[-1]):
                # If they are not anagrams, add the current word to the result.
                result.append(words[i])
                
        return result
    
#Time Complexity: O(n * m log m), where n is the number of words and m is the maximum length of a word.
#Space Complexity: O(n * m) for storing the result list in the worst case where no words are anagrams.