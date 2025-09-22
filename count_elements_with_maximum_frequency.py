#3005. Count Elements With Maximum Frequency

from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # 1. Count the frequency of each number using a Counter.
        freq_counter = Counter(nums)
        
        # 2. Find the maximum frequency.
        # The constraints state 1 <= nums.length, so freq_counter will not be empty.
        max_freq = max(freq_counter.values())
        
        # 3. Count how many elements share this maximum frequency.
        elements_with_max_freq = 0
        for freq in freq_counter.values():
            if freq == max_freq:
                elements_with_max_freq += 1
        
        # 4. The result is the max frequency multiplied by the number of elements that have it.
        return max_freq * elements_with_max_freq
    
#Time Complexity: O(n) where n is the length of nums
#Space Complexity: O(k) where k is the number of unique elements in nums