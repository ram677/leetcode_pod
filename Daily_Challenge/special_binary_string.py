#761. Special Binary String

class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        substrings = []
        
        # Iterate to find all independent, irreducible special substrings
        for i, char in enumerate(s):
            # Update balance: +1 for '1', -1 for '0'
            count += 1 if char == '1' else -1
            
            # When count is 0, we found a complete special string from `start` to `i`
            if count == 0:
                # The string is irreducible, so it starts with '1' and ends with '0'.
                # We extract the inner part, process it recursively, and reconstruct it.
                inner_str = s[start+1:i]
                processed_inner = self.makeLargestSpecial(inner_str)
                substrings.append('1' + processed_inner + '0')
                
                # Move the start pointer for the next special substring
                start = i + 1
                
        # Since we can swap any adjacent special substrings, we can sort them
        # in descending order to get the lexicographically largest result.
        substrings.sort(reverse=True)
        
        # Concatenate the sorted substrings
        return "".join(substrings)

# Time Complexity: O(n log n) due to sorting the substrings, where n is the length of the input string.
# Space Complexity: O(n) for storing the substrings and the recursive call stack.