#3354. Make Array Elements Equal to Zero

from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_count = 0

        # Step 1: Find all possible starting indices (where nums[i] is 0).
        zero_indices = [i for i, val in enumerate(nums) if val == 0]

        # Step 2: Simulate for each starting index and each possible direction.
        for start_pos in zero_indices:
            for start_dir in [-1, 1]:  # -1 for left, 1 for right
                
                # Create a copy of the array for this specific simulation.
                nums_copy = list(nums)
                curr = start_pos
                direction = start_dir

                # The simulation runs as long as the agent is within the array.
                while 0 <= curr < n:
                    if nums_copy[curr] > 0:
                        # Decrement, reverse, and move.
                        nums_copy[curr] -= 1
                        direction *= -1
                        curr += direction
                    else:  # nums_copy[curr] == 0
                        # Just move.
                        curr += direction

                # Step 3: After the simulation, check if it was a valid one.
                if all(val == 0 for val in nums_copy):
                    valid_count += 1
        
        # Step 4: Return the total count of valid selections.
        return valid_count
    
# Time Complexity:
# The solution involves iterating through the array multiple times for each starting position and direction. 
# In the worst case, for each zero position, we may traverse the entire array. Thus, the time complexity is O(k * n^2), where k is the number of zeros in the array and n is the length of the array.
# Space Complexity: O(n) due to the copy of the array used in each simulation.