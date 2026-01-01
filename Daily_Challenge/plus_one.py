#66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Iterate backwards from the last index
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        # If we reach here, it means all digits were 9 (e.g., 999 -> 000)
        # We need to add 1 at the beginning
        return [1] + digits
    
# Time Complexity: O(n), where n is the number of digits in the input list.
# Space Complexity: O(1) if we don't count the output list, otherwise O(n).