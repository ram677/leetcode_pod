#3003. Maximize the Number of Partitions After Operations

import sys
from typing import List

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        # We might encounter deep recursion, so it's safer to increase the limit.
        sys.setrecursionlimit(len(s) + 100)
        memo = {}
        n = len(s)

        # The state for our recursive DP is (index, current_partition_mask, change_used_flag)
        def solve(index, mask, changed):
            # Base Case: If we've processed the entire string, the last partition
            # we were building is now complete, so it counts as 1.
            if index == n:
                return 1

            state = (index, mask, changed)
            if state in memo:
                return memo[state]

            # --- Option 1: Keep the original character s[index] ---
            char_bit = 1 << (ord(s[index]) - ord('a'))
            new_mask_keep = mask | char_bit

            res_keep = 0
            if bin(new_mask_keep).count('1') > k:
                # If adding s[index] exceeds k distinct characters, we must start a new partition.
                res_keep = 1 + solve(index + 1, char_bit, changed)
            else:
                # Otherwise, continue the current partition.
                res_keep = solve(index + 1, new_mask_keep, changed)
            
            result = res_keep

            # --- Option 2: Use the one allowed change at s[index] (if available) ---
            if not changed:
                # Iterate through all 26 possible characters to change to.
                for i in range(26):
                    new_char_bit = 1 << i
                    new_mask_change = mask | new_char_bit
                    
                    current_res_change = 0
                    if bin(new_mask_change).count('1') > k:
                        # This change forces a new partition.
                        current_res_change = 1 + solve(index + 1, new_char_bit, True)
                    else:
                        # This change allows continuing the current partition.
                        current_res_change = solve(index + 1, new_mask_change, True)
                    
                    result = max(result, current_res_change)

            memo[state] = result
            return result

        # Initial call: start at index 0, with an empty mask, and the change is available.
        return solve(0, 0, False)
    
# Time Complexity: O(n * 2^k)
# Space Complexity: O(n * 2^k) due to memoization storage.
# where n is the length of the string and k is the maximum number of distinct characters allowed per partition.