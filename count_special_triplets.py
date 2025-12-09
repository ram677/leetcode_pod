#3583. Count Special Triplets

from collections import Counter

class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Initially, all numbers are "to the right" of our starting pointer
        right_map = Counter(nums)
        left_map = Counter()
        
        total_triplets = 0
        
        for num in nums:
            # 1. Remove the current number from the right side map
            #    because it is currently acting as the middle element 'j'
            right_map[num] -= 1
            
            # 2. Identify the value we need on the left (i) and right (k)
            target = num * 2
            
            # 3. Calculate how many valid triplets can be formed with 'num' as the center
            #    Counter returns 0 if the key is missing, which handles cases gracefully
            left_count = left_map[target]
            right_count = right_map[target]
            
            if left_count > 0 and right_count > 0:
                current_combinations = (left_count * right_count) % MOD
                total_triplets = (total_triplets + current_combinations) % MOD
            
            # 4. Add the current number to the left map for future iterations
            left_map[num] += 1
            
        return total_triplets
    
# Time Complexity: O(n), where n is the length of the input list.
# Space Complexity: O(n), for the two Counter dictionaries.