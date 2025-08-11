#2438. Range Product Queries of Powers

from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        # Step 1: extract powers of two
        powers = []
        bit = 0
        while n:
            if n & 1:
                powers.append(1 << bit)
            bit += 1
            n >>= 1

        # Step 2: precompute prefix products mod MOD
        prefix = [0] * len(powers)
        prod = 1
        for i, val in enumerate(powers):
            prod = (prod * val) % MOD
            prefix[i] = prod

        # Step 3: answer queries
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                val = prefix[r] * pow(prefix[l - 1], MOD - 2, MOD) % MOD
                ans.append(val)

        return ans

#Time Complexity: O(q + m) where q is the number of queries and m is the number of bits in n.
#Space Complexity: O(m) for the prefix product array.
#The space complexity is mainly due to the storage of the prefix product array, which has a size proportional to the number of bits in n.
# Note: The solution computes the product of powers of two in a range defined by queries, using modular arithmetic to handle large numbers.