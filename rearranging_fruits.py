#2561. Rearranging Fruits

from collections import Counter

class Solution:
    def minCost(self, basket1, basket2):
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        combined = count1 + count2

        for fruit in combined:
            if combined[fruit] % 2 != 0:
                return -1  # Impossible

        # Fruits to be moved from basket1 to basket2 and vice versa
        swap_from_b1 = []
        swap_from_b2 = []

        for fruit in combined:
            half = combined[fruit] // 2
            if count1[fruit] > half:
                swap_from_b1.extend([fruit] * (count1[fruit] - half))
            elif count2[fruit] > half:
                swap_from_b2.extend([fruit] * (count2[fruit] - half))

        if len(swap_from_b1) != len(swap_from_b2):
            return -1  # Should not happen if logic is correct

        swap_from_b1.sort()
        swap_from_b2.sort(reverse=True)

        min_fruit = min(basket1 + basket2)
        total_cost = 0
        for a, b in zip(swap_from_b1, swap_from_b2):
            # Choose the cheaper of direct swap or via 2 * min_fruit
            total_cost += min(min(a, b), 2 * min_fruit)

        return total_cost

#Time Complexity: O(n log n)
#Space Complexity: O(n)
#The variable n refers to the length of the input arrays.