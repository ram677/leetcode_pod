#966. Vowel Spellchecker

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Helper function to replace vowels with '*'
        def replace_vowels(word):
            vowels = "aeiou"
            result = []
            for char in word:
                if char.lower() in vowels:
                    result.append('*')
                else:
                    result.append(char.lower())
            return "".join(result)

        exact_set = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_map:
                case_map[lower_word] = word

            vowel_replaced = replace_vowels(word)
            if vowel_replaced not in vowel_map:
                vowel_map[vowel_replaced] = word
        
        answers = []
        for query in queries:
            # Rule 1: Exact match
            if query in exact_set:
                answers.append(query)
                continue

            # Rule 2: Case-insensitive match
            lower_query = query.lower()
            if lower_query in case_map:
                answers.append(case_map[lower_query])
                continue

            # Rule 3: Vowel error match
            vowel_replaced_query = replace_vowels(query)
            if vowel_replaced_query in vowel_map:
                answers.append(vowel_map[vowel_replaced_query])
                continue

            # No match
            answers.append("")
        
        return answers
    
#Time Complexity: O(m + n), where m is the total length of words in wordlist and n is the total length of words in queries.
#Space Complexity: O(m), for storing the sets and maps.