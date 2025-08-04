#904. Fruit Into Baskets

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        max_fruits = 0
        start = 0

        for end in range(len(fruits)):
            basket[fruits[end]] += 1

            # Shrink window if we have more than 2 types
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits

#Time Complexity: O(n), where n is the length of fruits
#Space Complexity: O(1), since the number of fruit types is limited (at most 2 types in this problem).