#3147. Taking Maximum Energy From the Mystic Dungeon

from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        
        # We iterate backwards from the end of the array.
        # The last k elements are the base cases, as their paths have only one step.
        # For any index i, we update energy[i] to store the total sum of the path starting at i.
        for i in range(n - 1, -1, -1):
            # Check if a next magician exists in the teleportation sequence.
            if i + k < n:
                # The total energy for a path starting at i is its own energy
                # plus the total energy of the path starting from the next stop (i+k).
                # Since we are iterating backwards, energy[i+k] already holds this total.
                energy[i] += energy[i + k]
                
        # After the loop, energy[i] stores the total energy for each possible start.
        # The answer is the maximum among all possible starting points.
        return max(energy)

# Time Complexity: O(n) where n is the length of energy.
# Space Complexity: O(1) as we are modifying the input array in place.