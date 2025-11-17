#1437. Check If All 1's Are at Least Length K Places Away

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Initialize the position of the previously seen '1' to -1
        last_pos = -1
        
        for i, num in enumerate(nums):
            if num == 1:
                # If we have seen a '1' before (last_pos is not -1),
                # check the distance between the current '1' and the previous '1'.
                if last_pos != -1:
                    # The number of spaces between two indices i and j is (i - j - 1).
                    # If this gap is strictly less than k, the condition fails.
                    if i - last_pos - 1 < k:
                        return False
                
                # Update the last seen position to the current index
                last_pos = i
                
        return True
    
# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1), as we are using only a constant amount of extra space.