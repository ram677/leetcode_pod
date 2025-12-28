#3397. Maximum Number of Distinct Elements After Operations

import collections
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        """
        Calculates the maximum possible distinct elements using a greedy strategy.
        """
        # Step 1: Count frequencies and get sorted unique numbers.
        counts = collections.Counter(nums)
        unique_sorted = sorted(counts.keys())
        
        distinct_count = 0
        # Tracks the last integer slot that has been filled. Initialize to a very small number.
        last_occupied = float('-inf')

        # Step 2: Iterate through unique numbers and greedily place their copies.
        for x in unique_sorted:
            count = counts[x]
            
            # Determine the first possible slot for the current number x.
            # It must be within x's range [x-k, ...] and after the last occupied slot.
            start_slot = max(x - k, last_occupied + 1)
            
            # The last possible slot for the current number x.
            end_slot = x + k
            
            # We can't place more copies than we have, or more than the number of
            # available integer slots in our valid range.
            if start_slot > end_slot:
                # No available slots for this number.
                num_to_place = 0
            else:
                available_slots = end_slot - start_slot + 1
                num_to_place = min(count, available_slots)
            
            # If we successfully place any copies, update our count and the last occupied slot.
            if num_to_place > 0:
                distinct_count += num_to_place
                last_occupied = start_slot + num_to_place - 1
                
        return distinct_count
    
#Time Complexity: O(n log n) due to sorting the unique elements.
#Space Complexity: O(n) for storing counts and unique elements.
# where n is the length of the input list nums.