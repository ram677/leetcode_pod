#3652. Best Time to Buy and Sell Stock using Strategy

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        
        # 1. Calculate the initial profit without any modification
        current_profit = 0
        for p, s in zip(prices, strategy):
            current_profit += p * s
            
        # 2. Setup Sliding Window
        # The window size is k. Half size is m.
        m = k // 2
        
        # We need to compute the "delta" (change in profit) if we apply the mod.
        # Delta = (New contributions in window) - (Old contributions in window)
        #
        # For first half (indices i to i+m-1): 
        #   New strategy is 0. New contribution is 0. 
        #   Change is: 0 - (prices[x] * strategy[x])
        #
        # For second half (indices i+m to i+k-1):
        #   New strategy is 1. New contribution is prices[x].
        #   Change is: prices[x] - (prices[x] * strategy[x])
        
        # Initialize the first window (indices 0 to k-1)
        # sum_first_half corresponds to sum(prices[x] * strategy[x]) to be REMOVED
        sum_first_half = 0
        for i in range(m):
            sum_first_half += prices[i] * strategy[i]
            
        # sum_second_half corresponds to sum(prices[x] * (1 - strategy[x])) to be ADDED
        # (This is derived from: New_Val - Old_Val = price - price*strategy)
        sum_second_half = 0
        for i in range(m, k):
            sum_second_half += prices[i] * (1 - strategy[i])
            
        # Track the maximum improvement found
        max_delta = sum_second_half - sum_first_half
        
        # 3. Slide the window across the array
        # The window starts at index i.
        # Current window covers [i, i+k-1].
        # Next window covers [i+1, i+k].
        
        # Current 'first half' ends at i+m-1. 
        # Current 'second half' ends at i+k-1.
        
        for i in range(n - k):
            # Element leaving the FIRST half: index i
            leaving_first = i
            sum_first_half -= prices[leaving_first] * strategy[leaving_first]
            
            # Element moving from SECOND half to FIRST half: index i + m
            moving_idx = i + m
            # Add its contribution to sum_first_half (as it is now in the first half)
            sum_first_half += prices[moving_idx] * strategy[moving_idx]
            # Remove its contribution from sum_second_half (it is no longer in second half)
            sum_second_half -= prices[moving_idx] * (1 - strategy[moving_idx])
            
            # Element entering the SECOND half: index i + k
            entering_second = i + k
            sum_second_half += prices[entering_second] * (1 - strategy[entering_second])
            
            # Calculate new delta
            current_delta = sum_second_half - sum_first_half
            if current_delta > max_delta:
                max_delta = current_delta
                
        # If the best modification reduces profit, we don't perform it (max with 0)
        return current_profit + max(0, max_delta)
    
# Time Complexity: O(n), where n is the length of prices.
# Space Complexity: O(1), we use a constant amount of extra space.