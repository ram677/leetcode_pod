#3719. Longest Balanced Subarray I

from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Iterate over all possible starting points of the subarray
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            # Extend the subarray from i to j
            for j in range(i, n):
                num = nums[j]
                
                # Check parity and add to respective set
                if num % 2 == 0:
                    distinct_evens.add(num)
                else:
                    distinct_odds.add(num)
                
                # If the counts of distinct evens and odds are equal, update max_len
                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len
    
# Time Complexity: O(n^2) - We have two nested loops to check all subarrays.
# Space Complexity: O(n) - In the worst case, we might store all distinct numbers in the sets.