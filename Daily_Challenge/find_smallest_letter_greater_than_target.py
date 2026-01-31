#744. Find Smallest Letter Greater Than Target

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        n = len(letters)
        
        while left < right:
            mid = (left + right) // 2
            
            # We are looking for the smallest element strictly greater than target.
            # If the current element is <= target, the answer must be to the right.
            if letters[mid] <= target:
                left = mid + 1
            # If the current element is > target, it could be the answer,
            # or the answer could be to the left.
            else:
                right = mid
                
        # Use modulo to handle the wrap-around case.
        # If left == n (target is larger than all elements), it wraps to 0.
        return letters[left % n]
    
# Time Complexity: O(log n) where n is the number of letters.
# Space Complexity: O(1).