#3318. Find X-Sum of All K-Long Subarrays I

import collections
from typing import List

class Solution:
    
    def _calculate_x_sum(self, subarray: List[int], x: int) -> int:
        """Helper function to calculate the x-sum for a single subarray."""
        
        # 1. Count frequencies
        counts = collections.Counter(subarray)
        distinct_elements = list(counts.keys())
        
        # 2. Handle the edge case where distinct elements < x
        if len(distinct_elements) < x:
            return sum(subarray)
            
        # 3. Sort the distinct elements
        # Primary key: frequency (descending)
        # Secondary key: value (descending)
        def sort_key(element):
            return (-counts[element], -element)
            
        distinct_elements.sort(key=sort_key)
        
        # 4. Get the set of the top x most frequent elements
        top_x_elements = set(distinct_elements[:x])
        
        # 5. Calculate the sum of all occurrences of these top x elements
        total_sum = 0
        for num in subarray:
            if num in top_x_elements:
                total_sum += num
                
        return total_sum

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        
        # Iterate through all possible starting positions
        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            
            # Calculate the x-sum for this subarray
            current_x_sum = self._calculate_x_sum(subarray, x)
            answer.append(current_x_sum)
            
        return answer
    
# Time Complexity: O(n * k log k), where n is the length of nums and k is the subarray length.
# Space Complexity: O(k), for storing the frequency counts and distinct elements.