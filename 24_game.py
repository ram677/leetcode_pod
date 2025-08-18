#679. 24 Game.

from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6  # small tolerance for floating point errors

        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            # Try all pairs of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Remaining numbers after removing nums[i] and nums[j]
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                        # Try all operations
                        for op in self.compute(nums[i], nums[j]):
                            if backtrack(next_nums + [op]):
                                return True
            return False

        return backtrack(cards)

    def compute(self, a, b):
        """Return all possible results of applying +, -, *, / on a and b."""
        results = [a + b, a - b, b - a, a * b]
        if abs(b) > 1e-6:  # avoid divide by zero
            results.append(a / b)
        if abs(a) > 1e-6:
            results.append(b / a)
        return results

#Time Complexity: O(1)
#Space Complexity: O(1)