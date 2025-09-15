#1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Create a set of broken letters for efficient lookups.
        broken_set = set(brokenLetters)
        
        # Split the input text into a list of words.
        words = text.split(' ')
        
        # This will be our counter for the words that can be fully typed.
        typeable_words_count = 0
        
        # Iterate over each word in the list.
        for word in words:
            # Assume the word is typeable until we find a broken letter.
            is_typeable = True
            
            # Check each character in the current word.
            for char in word:
                # If a character is in the broken set, the word is not typeable.
                if char in broken_set:
                    is_typeable = False
                    # Once we find one broken letter, we can stop checking this word.
                    break
            
            # If the word was determined to be typeable, increment our counter.
            if is_typeable:
                typeable_words_count += 1
                
        return typeable_words_count
    
#Time Complexity: O(n*m), where n is the number of words and m is the average length of the words.
#Space Complexity: O(b), where b is the number of broken letters (at most 26).