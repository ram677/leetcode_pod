#1716. Calculate Money in Leetcode Bank

from typing import List

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        # Iterate through each day, from day 0 to n-1.
        for day in range(n):
            # Determine the week number (0-indexed).
            week = day // 7
            # Determine the day within the week (0 for Monday, 1 for Tuesday, etc.).
            day_of_week = day % 7
            
            # The deposit consists of the base amount for that week's Monday
            # plus the daily increment.
            deposit = (week + 1) + day_of_week
            total += deposit
            
        return total
    
#Time Complexity: O(n) where n is the number of days.
#Space Complexity: O(1) since we are using a constant amount of extra space.