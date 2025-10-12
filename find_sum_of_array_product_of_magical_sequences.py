#3539. Find Sum of Array Product of Magical Sequences

from typing import List

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute combinations C(n, k)
        C = [[0] * (m + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        memo = {}

        def solve(j: int, items_left: int, carry: int) -> tuple:
            # Base Case: All indices considered
            if j == n:
                # If we used exactly m items, calculate bits from the final carry
                if items_left == 0:
                    bits = bin(carry).count('1')
                    if bits <= k:
                        res = [0] * (k + 1)
                        res[bits] = 1
                        return tuple(res)
                return tuple([0] * (k + 1))

            state = (j, items_left, carry)
            if state in memo:
                return memo[state]

            # ans[b] = sum of products for this subproblem with 'b' set bits
            ans = [0] * (k + 1)
            
            # Iterate on c_j: how many times we pick index 'j'
            for c_j in range(items_left + 1):
                # Number of ways to choose c_j items from items_left
                ways = C[items_left][c_j]
                
                # Product contribution from these c_j items
                prod_part = pow(nums[j], c_j, MOD)
                
                # Term combining ways and product
                term = (ways * prod_part) % MOD
                
                # Recursive call for the next index
                sub_res_tuple = solve(j + 1, items_left - c_j, (carry + c_j) // 2)
                
                # Current bit determined by this step
                current_bit = (carry + c_j) % 2
                
                # Combine results
                for bits_from_sub in range(k + 1 - current_bit):
                    if sub_res_tuple[bits_from_sub] > 0:
                        total_bits = bits_from_sub + current_bit
                        contribution = (term * sub_res_tuple[bits_from_sub]) % MOD
                        ans[total_bits] = (ans[total_bits] + contribution) % MOD

            memo[state] = tuple(ans)
            return memo[state]

        # Initial call: start at index 0, with m items to choose, and 0 carry.
        final_result_tuple = solve(0, m, 0)
        return final_result_tuple[k]

# Time Complexity: O(n * m^2 * k) in the worst case due to the recursive calls and combinations.
# Space Complexity: O(n * m * k) for memoization and combination table.