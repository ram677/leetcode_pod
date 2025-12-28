# 808. Soup Servings

from functools import lru_cache
import math

class Solution:
    def soupServings(self, n: int) -> float:
        # Quick cutoff for very large n where probability -> 1
        if n > 4800:
            return 1.0

        units = math.ceil(n / 25)

        @lru_cache(None)
        def f(a: int, b: int) -> float:
            # base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25 * (
                f(a - 4, b) +
                f(a - 3, b - 1) +
                f(a - 2, b - 2) +
                f(a - 1, b - 3)
            )

        return f(units, units)

# Time Complexity: O(n^2) due to the recursive calls and memoization.
# Space Complexity: O(n) for the memoization cache
# Note: The solution uses memoization to optimize the recursive calls, which significantly reduces the number of computations needed.
#       and allows the function to handle larger values of n efficiently.   
#       The cutoff for n > 4800 is based on the observation that the probability approaches 1 as n increases.
#       The function f(a, b) computes the probability of finishing the soup servings given a and b units of soup A and B respectively.
#       The function is designed to handle the soup servings problem efficiently using dynamic programming principles.