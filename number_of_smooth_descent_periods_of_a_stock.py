#2110. Number of Smooth Descent Periods of a Stock

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # Initialize total count and current streak length
        # We start with the first element effectively processed (streak of 1)
        total_periods = 1
        current_streak = 1
        
        for i in range(1, len(prices)):
            # Check if the current price is exactly 1 less than the previous
            if prices[i-1] - prices[i] == 1:
                current_streak += 1
            else:
                # Reset streak if the pattern breaks
                current_streak = 1
            
            # Add the number of valid periods ending at the current index
            total_periods += current_streak
            
        return total_periods

# Time Complexity: O(n), where n is the length of the prices list.
# Space Complexity: O(1), as we use only a constant amount of extra space.