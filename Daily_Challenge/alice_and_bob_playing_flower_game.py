#3021. Alice and Bob Playing Flower Game

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        Calculates the number of pairs (x, y) for which Alice wins.
        Alice wins if the total number of turns (x + y) is odd.
        """
        
        # We need to count pairs where one number is even and the other is odd.
        
        # Method 1: Explicit Counting
        # n_evens = n // 2
        # n_odds = (n + 1) // 2
        # m_evens = m // 2
        # m_odds = (m + 1) // 2
        #
        # return (n_evens * m_odds) + (n_odds * m_evens)
        
        # Method 2: Simplified Formula
        # The number of pairs (x, y) where x + y is odd out of a total
        # of n * m pairs is always floor((n * m) / 2).
        
        return (n * m) // 2

# Time Complexity: O(1)
# Space Complexity: O(1)