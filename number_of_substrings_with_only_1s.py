#1513. Number of Substrings With Only 1s

from typing import List

class Solution:
    def numSub(self, s: str) -> int:
        
        total_substrings = 0
        current_streak = 0
        MOD = 10**9 + 7
        
        for char in s:
            if char == '1':
                # We found a '1', so we've found 'current_streak' new substrings
                # that end at this position.
                current_streak += 1
                total_substrings = (total_substrings + current_streak) % MOD
            else:
                # The streak is broken
                current_streak = 0
                
        return total_substrings