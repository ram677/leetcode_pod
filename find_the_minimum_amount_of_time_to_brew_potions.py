#3494. Find the Minimum Amount of Time to Brew Potions

from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        # 1. Precompute the prefix sums of the skill array.
        prefix_skill = [0] * n
        current_sum = 0
        for i in range(n):
            current_sum += skill[i]
            prefix_skill[i] = current_sum

        # 2. Iteratively calculate the start time for each potion.
        # current_potion_start_time represents S_j.
        current_potion_start_time = 0
        
        for j in range(1, m):
            mana_prev = mana[j - 1]
            mana_curr = mana[j]
            
            # Find the maximum delay term from the recurrence relation.
            max_delay_term = 0
            for i in range(n):
                p_i = prefix_skill[i]
                p_i_minus_1 = prefix_skill[i - 1] if i > 0 else 0
                
                delay_term = p_i * mana_prev - p_i_minus_1 * mana_curr
                if delay_term > max_delay_term:
                    max_delay_term = delay_term
            
            # Update the start time for the next potion.
            current_potion_start_time += max_delay_term

        # 3. Calculate the final finish time.
        total_skill = prefix_skill[n - 1]
        finish_time = current_potion_start_time + total_skill * mana[m - 1]
        
        return finish_time

# Time Complexity: O(n * m) where n is the length of skill and m is the length of mana.
# Space Complexity: O(n) for the prefix_skill array.