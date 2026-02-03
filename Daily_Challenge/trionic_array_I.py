#3637. Trionic Array I

from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Iterate through all valid p and q.
        # 0 < p < q < n - 1 implies:
        # p can range from 1 to n - 3 (leaving room for at least one q and the end)
        # q can range from p + 1 to n - 2 (leaving room for the end)
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                
                # 1. Check if nums[0...p] is strictly increasing
                # We check pairs (i, i+1) from 0 up to p-1
                if any(nums[i] >= nums[i+1] for i in range(p)):
                    continue
                
                # 2. Check if nums[p...q] is strictly decreasing
                # We check pairs (i, i+1) from p up to q-1
                if any(nums[i] <= nums[i+1] for i in range(p, q)):
                    continue
                    
                # 3. Check if nums[q...n-1] is strictly increasing
                # We check pairs (i, i+1) from q up to n-2
                if any(nums[i] >= nums[i+1] for i in range(q, n - 1)):
                    continue
                
                # If all conditions pass, we found a valid split
                return True
                
        return False
    
# Time Complexity: O(n^3) in the worst case due to nested loops and checks, where n is the length of nums.
# Space Complexity: O(1).