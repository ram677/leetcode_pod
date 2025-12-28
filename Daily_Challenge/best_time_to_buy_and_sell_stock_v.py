#3573. Best Time to Buy and Sell Stock V

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # We need three arrays to track the max profit for each transaction count j (1 to k).
        # dp[j]: Max profit with j transactions completed (Neutral state)
        # hold[j]: Max profit with j-th transaction in progress (Long/Holding position)
        # short[j]: Max profit with j-th transaction in progress (Short position)
        
        # Initialize: 0 profit for neutral, -inf for active positions (impossible at start)
        dp = [0] * (k + 1)
        hold = [float('-inf')] * (k + 1)
        short = [float('-inf')] * (k + 1)
        
        for price in prices:
            # Create copies to represent the state of the "previous day".
            # This ensures we don't use a transaction closed TODAY to open a new one TODAY.
            prev_dp = dp[:]
            prev_hold = hold[:]
            prev_short = short[:]
            
            for j in range(1, k + 1):
                # 1. Update Neutral State (finished j-th transaction)
                # Options: Stay neutral, Sell Long position (+price), or Buy Back Short position (-price)
                dp[j] = max(prev_dp[j], prev_hold[j] + price, prev_short[j] - price)
                
                # 2. Update Long State (working on j-th transaction)
                # Options: Continue holding, or Buy new stock (-price) starting from (j-1) completed transactions
                hold[j] = max(prev_hold[j], prev_dp[j-1] - price)
                
                # 3. Update Short State (working on j-th transaction)
                # Options: Continue shorting, or Sell Short (+price) starting from (j-1) completed transactions
                short[j] = max(prev_short[j], prev_dp[j-1] + price)
                
        # The answer is the max profit having completed at most k transactions (Neutral state)
        return dp[k]
    
# Time Complexity: O(n*k), where n is the number of days and k is the max transactions.
# Space Complexity: O(k) due to the three arrays of size k+1.