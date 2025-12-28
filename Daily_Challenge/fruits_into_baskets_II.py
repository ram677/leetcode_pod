#3477. Fruits Into Baskets II

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n  # Track which baskets are used
        unplaced = 0

        for i in range(n):
            placed = False
            for j in range(n):
                if not used[j] and baskets[j] >= fruits[i]:
                    used[j] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1

        return unplaced

#Time Complexity: O(n^2), where n is the length of fruits
#Space Complexity: O(n), for the used list to track basket usage.