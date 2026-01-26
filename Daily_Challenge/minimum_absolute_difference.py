#1200. Minimum Absolute Difference

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to ensure minimum differences are between adjacent elements
        arr.sort()
        
        min_diff = float('inf')
        result = []
        
        # Step 2: Iterate through adjacent pairs
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            
            # Case 1: Found a new smaller difference
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]] # Start a new list with this pair
            
            # Case 2: Found a pair with the same minimum difference
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result
    
# Time Complexity: O(n log n) due to sorting, where n is the length of the input array.
# Space Complexity: O(1) if we ignore the output storage, as we are sorting in place.