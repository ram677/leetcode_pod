#3562. Maximum Profit from Trading Stocks with Discounts

import math
from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build adjacency list for the tree
        children = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            children[u].append(v)
            
        # Helper to merge two DP arrays (Knapsack merge)
        # dp1: current accumulated results
        # dp2: new child's results
        def merge(dp1, dp2):
            new_dp = [-float('inf')] * (budget + 1)
            
            # Find indices where states are reachable to optimize inner loops
            valid_b1 = [i for i, x in enumerate(dp1) if x != -float('inf')]
            valid_b2 = [i for i, x in enumerate(dp2) if x != -float('inf')]
            
            for b1 in valid_b1:
                val1 = dp1[b1]
                for b2 in valid_b2:
                    if b1 + b2 <= budget:
                        if val1 + dp2[b2] > new_dp[b1 + b2]:
                            new_dp[b1 + b2] = val1 + dp2[b2]
            return new_dp

        def dfs(u):
            # 1. Aggregate results from all children
            # We maintain two aggregate states for the children of u:
            # dp_children_bought: Max profit from ALL children subtrees assuming u IS bought
            # dp_children_skipped: Max profit from ALL children subtrees assuming u IS NOT bought
            
            # Base case: 0 cost, 0 profit
            dp_children_bought = [-float('inf')] * (budget + 1)
            dp_children_bought[0] = 0
            
            dp_children_skipped = [-float('inf')] * (budget + 1)
            dp_children_skipped[0] = 0
            
            for v in children[u]:
                # Recursively get the two scenarios from child v
                # child_res_..._bought: v's result if u (v's parent) bought
                # child_res_..._skipped: v's result if u (v's parent) skipped
                child_res_if_parent_bought, child_res_if_parent_skipped = dfs(v)
                
                # Merge into the running totals for u
                dp_children_bought = merge(dp_children_bought, child_res_if_parent_bought)
                dp_children_skipped = merge(dp_children_skipped, child_res_if_parent_skipped)
            
            # 2. Calculate costs and profits for node u
            p_idx = u - 1
            cost_full = present[p_idx]
            cost_half = cost_full // 2
            profit_full = future[p_idx] - cost_full
            profit_half = future[p_idx] - cost_half
            
            # 3. Construct the two result arrays to return to u's parent
            res_parent_bought = [-float('inf')] * (budget + 1)
            res_parent_skipped = [-float('inf')] * (budget + 1)
            
            # --- Scenario 1: u's parent BOUGHT their stock (u gets discount) ---
            # Option A: We BUY u (cost: half)
            for b, profit in enumerate(dp_children_bought):
                if profit == -float('inf'): continue
                total_cost = b + cost_half
                if total_cost <= budget:
                    total_profit = profit + profit_half
                    if total_profit > res_parent_bought[total_cost]:
                        res_parent_bought[total_cost] = total_profit
            
            # Option B: We SKIP u (cost: 0)
            for b, profit in enumerate(dp_children_skipped):
                if profit == -float('inf'): continue
                # total_cost = b + 0, total_profit = profit + 0
                if profit > res_parent_bought[b]:
                    res_parent_bought[b] = profit

            # --- Scenario 2: u's parent SKIPPED their stock (u pays full) ---
            # Option A: We BUY u (cost: full)
            for b, profit in enumerate(dp_children_bought):
                if profit == -float('inf'): continue
                total_cost = b + cost_full
                if total_cost <= budget:
                    total_profit = profit + profit_full
                    if total_profit > res_parent_skipped[total_cost]:
                        res_parent_skipped[total_cost] = total_profit
            
            # Option B: We SKIP u (cost: 0)
            for b, profit in enumerate(dp_children_skipped):
                if profit == -float('inf'): continue
                if profit > res_parent_skipped[b]:
                    res_parent_skipped[b] = profit
                        
            return res_parent_bought, res_parent_skipped

        # The root is Employee 1. They have no parent, so they always pay full price.
        # This corresponds to the "parent skipped" scenario.
        _, root_res = dfs(1)
        
        # Return the max profit found within the budget (at least 0)
        return max(0, max(root_res))
    
# Time Complexity: O(n * budget^2) in the worst case due to merging DP arrays, where n is the number of employees and budget is the maximum budget.
# Space Complexity: O(n * budget) for storing DP states for each node.