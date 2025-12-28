#1590. Make Sum Divisible by P

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        target = total_sum % p
        
        if target == 0:
            return 0
        
        # Dictionary to store {remainder: index}
        # Initialize with {0: -1} to handle cases where the subarray starts from index 0
        last_seen = {0: -1}
        
        current_sum = 0
        min_len = n
        
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            
            # We want to find a previous prefix sum such that:
            # (current_sum - previous_sum) % p == target
            # Therefore: previous_sum % p == (current_sum - target) % p
            needed = (current_sum - target + p) % p
            
            if needed in last_seen:
                length = i - last_seen[needed]
                if length < min_len:
                    min_len = length
            
            # Update the last seen index for the current remainder
            last_seen[current_sum] = i
            
        if min_len == n:
            return -1
        
        return min_len
    
# Time Complexity: O(n), where n is the length of nums.
# Space Complexity: O(p), for the last_seen dictionary, where p is the modulus.