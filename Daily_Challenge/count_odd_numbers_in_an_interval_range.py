#1523. Count Odd Numbers in an Interval Range

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # The number of odds from 0 to n is (n + 1) // 2
        # We calculate odds up to 'high', and subtract odds up to 'low - 1'.
        # Note: count(0 to low-1) is ((low - 1) + 1) // 2, which simplifies to low // 2.
        return (high + 1) // 2 - low // 2
    
# Time Complexity: O(1)
# Space Complexity: O(1)