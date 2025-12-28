#3234. Count the Number of Substrings With Dominant Ones

import bisect
from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        total_count = 0
        
        # --- Case A: Count substrings with 0 zeros ---
        one_streak = 0
        for char in s:
            if char == '1':
                one_streak += 1
            else:
                total_count += one_streak * (one_streak + 1) // 2
                one_streak = 0
        # Add the last streak
        total_count += one_streak * (one_streak + 1) // 2
        
        # --- Case B: Count substrings with 1 <= zeros <= Z ---
        Z = int(n**0.5)
        zero_indices = [k for k, char in enumerate(s) if char == '0']
        num_zeros = len(zero_indices)
        
        # We can maintain a pointer `start_k` to avoid repeated binary searches
        start_k = 0 
        for i in range(n): # i is the start of the substring
            # Advance start_k to the first '0' at or after index i
            while start_k < num_zeros and zero_indices[start_k] < i:
                start_k += 1
                
            for z in range(1, Z + 1): # z is the number of zeros
                # Find the index of the z-th zero (in zero_indices)
                end_k = start_k + z - 1
                
                if end_k >= num_zeros:
                    # Not enough zeros left in the string to make z
                    break
                    
                # The index (in s) of the z-th zero
                j_zero = zero_indices[end_k]
                
                # The index (in s) of the boundary (the (z+1)-th zero or n)
                j_boundary = zero_indices[end_k + 1] if end_k + 1 < num_zeros else n
                
                # We need ones >= z*z
                # (j - i + 1) - z >= z*z
                # j >= z*z + z + i - 1
                required_j = z*z + z + i - 1
                
                # The start of our valid `j` range
                j_start = max(j_zero, required_j)
                
                # The end of our valid `j` range
                j_end = j_boundary - 1
                
                if j_start <= j_end:
                    total_count += (j_end - j_start + 1)
                    
        return total_count
    
# Time Complexity: O(n * sqrt(n)) in the worst case due to the nested loops.
# Space Complexity: O(m) where m is the number of '0's in the string.