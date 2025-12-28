#2785. Sort Vowels in a String

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Step 1: Extract all vowels
        found_vowels = []
        for char in s:
            if char in vowels:
                found_vowels.append(char)
        
        # Step 2: Sort the extracted vowels
        found_vowels.sort()
        
        # Step 3: Reconstruct the string
        result_list = list(s)
        vowel_ptr = 0
        
        for i in range(len(result_list)):
            if result_list[i] in vowels:
                result_list[i] = found_vowels[vowel_ptr]
                vowel_ptr += 1
                
        return "".join(result_list)

#Time Complexity: O(LlogV), where L is the length of the string and V is the number of vowels in the string.
#Space Complexity: O(L), where L is the length of the string.