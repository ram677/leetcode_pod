#1461. Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Total number of unique binary codes of length k is 2^k
        required_count = 1 << k
        
        # Optimization: If the string is too short, it can't hold all combinations
        if len(s) - k + 1 < required_count:
            return False
            
        # Set to keep track of the unique substrings we have seen
        seen = set()
        
        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            # Extract the substring and add to the set
            seen.add(s[i:i+k])
            
            # Early exit: if we have found all required combinations, return True
            if len(seen) == required_count:
                return True
                
        # If we finish the loop and haven't found all combinations
        return False

# Time Complexity: O(n) where n is the length of the string, since we are iterating through it once.
# Space Complexity: O(2^k) in the worst case, if all combinations are present in the string.