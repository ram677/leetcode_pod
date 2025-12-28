#2106. Maximum Fruits Harvested After at Most K Steps

from typing import List
import bisect

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        left = 0
        total = 0
        max_fruits = 0

        for right in range(n):
            total += fruits[right][1]

            # Shrink window from the left if it exceeds allowed k steps
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]

                # Minimum steps to cover [l_pos, r_pos] from startPos
                min_steps = min(
                    abs(startPos - l_pos) + (r_pos - l_pos),
                    abs(startPos - r_pos) + (r_pos - l_pos)
                )

                if min_steps <= k:
                    break
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits

#Time Complexity: O(n) (Each element is added and removed from the window at most once.)
#Space Complexity: O(1) (Only a few variables used. If prefix sum is used (alternative approach), space becomes O(n).)
#n refers to the number of fruit positions available — i.e., the length of the fruits list.
