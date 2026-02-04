#3640. Trionic Array II

from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        # Standard check, though constraints say n >= 4
        if n < 4:
            return 0
            
        # 1. DP Left: Max sum of increasing subarray ending at i
        # dp_inc[i] stores the max sum of a strictly increasing suffix ending at i
        dp_inc = [0] * n
        dp_inc[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # If extending is beneficial (positive sum), extend. Else start new.
                dp_inc[i] = nums[i] + max(0, dp_inc[i-1])
            else:
                dp_inc[i] = nums[i]
                
        # 2. DP Right: Max sum of increasing subarray starting at i
        dp_inc_start = [0] * n
        dp_inc_start[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                dp_inc_start[i] = nums[i] + max(0, dp_inc_start[i+1])
            else:
                dp_inc_start[i] = nums[i]
                
        # 3. Prefix Sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]
            
        ans = -float('inf')
        max_p_val = -float('inf')
        
        # 4. Iterate to find optimal p and q connected by a decreasing segment
        # We iterate 'k'. 
        # - k can act as 'q' if valid.
        # - k can act as 'p' for future indices.
        # - If the decreasing chain breaks, we reset our memory of 'p'.
        
        for k in range(n):
            # Check continuity of decreasing segment:
            # If nums[k] >= nums[k-1], the strictly decreasing run from previous indices is broken.
            # Thus, any 'p' found before 'k' cannot connect to 'k' or any index after 'k'.
            if k > 0 and nums[k] >= nums[k-1]:
                max_p_val = -float('inf')
            
            # CASE Q: Try to treat current index 'k' as 'q'
            # Must satisfy: q < r (has valid right neighbor) and nums[q] < nums[q+1] (start of increasing)
            if k < n - 1 and nums[k] < nums[k+1]:
                # We need a valid p from the current decreasing run
                if max_p_val != -float('inf'):
                    # The term for q is: sum(q...r) - nums[q] + prefix[q+1] (part of middle sum logic)
                    # From derivation: Total = (S1[p] - nums[p]) + Sum(p...q) + (S3[q] - nums[q])
                    # Optimized: Total = (dp_inc[p-1] - pref[p]) + (pref[q+1] + dp_inc_start[q+1])
                    
                    # Here max_p_val stores max(dp_inc[p-1] - pref[p])
                    val_q = dp_inc_start[k+1] + pref[k+1]
                    ans = max(ans, max_p_val + val_q)
            
            # CASE P: Try to treat current index 'k' as 'p' for future use
            # Must satisfy: l < p (has valid left neighbor) and nums[p] > nums[p-1] (end of increasing)
            if k > 0 and nums[k] > nums[k-1]:
                # We calculate the potential contribution of p
                # Note: We use dp_inc[k-1] because the segment l...p sums to nums[p] + dp_inc[k-1]
                # P contribution to formula = dp_inc[k-1] - pref[k]
                current_p_val = dp_inc[k-1] - pref[k]
                max_p_val = max(max_p_val, current_p_val)
                
        return ans
    
# Time Complexity: O(n) due to single pass for DP and prefix sums, and single pass for finding optimal p and q, where n is the length of nums.
# Space Complexity: O(n) for the DP arrays and prefix sums.