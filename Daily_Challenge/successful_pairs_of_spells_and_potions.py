#2300. Successful Pairs of Spells and Potions

import bisect
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array to allow for efficient binary searching.
        potions.sort()
        m = len(potions)
        answer = []

        for spell in spells:
            # Calculate the minimum potion strength required to achieve success.
            # We use ceiling division to handle non-integer results.
            min_potion_strength = (success + spell - 1) // spell
            
            # Use binary search to find the insertion point for the required
            # potion strength. This gives us the index of the first potion
            # that is strong enough.
            index = bisect.bisect_left(potions, min_potion_strength)
            
            # The number of successful pairs is the number of potions from
            # this index to the end of the array.
            count = m - index
            answer.append(count)
            
        return answer
    
# Time Complexity: O(m log m + n log m) where n is the number of spells and m is the number of potions.
# Space Complexity: O(1) if we ignore the output list, otherwise O(n) for the output list.