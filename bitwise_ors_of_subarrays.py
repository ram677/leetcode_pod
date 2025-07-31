#898: Bitwise ORs of Subarrays

from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = set()

        for x in arr:
            cur = {x}
            for y in prev:
                cur.add(x | y)
            res.update(cur)
            prev = cur

        return len(res)
    
# Time Complexity: O(n * log(max(arr)))
# Space Complexity: O(n * log(max(arr)))
# n is the length of the input list arr, and max(arr) is the maximum value in the array.