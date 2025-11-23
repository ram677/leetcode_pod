#1262. Greatest Sum Divisible by Three

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i] stores the maximum sum we've found so far that has a remainder of i when divided by 3.
        # We initialize dp[0] to 0 (sum 0 has remainder 0).
        # We initialize dp[1] and dp[2] to -infinity (or a very small number) because
        # we haven't found any sums with those remainders yet.
        dp = [0, float('-inf'), float('-inf')]

        for num in nums:
            # Create a copy of the current dp state so we don't overwrite values 
            # we need for the current number's calculations.
            current_dp = dp[:]
            
            for s in current_dp:
                # Try adding the current number 'num' to each of our existing valid sums.
                current_sum = s + num
                
                # Calculate the remainder of this new sum
                remainder = current_sum % 3
                
                # Update the dp table for this remainder. We only keep the larger value:
                # either the old sum with this remainder, or our new current_sum.
                dp[remainder] = max(dp[remainder], current_sum)
        
        # The answer is the maximum sum with remainder 0
        return dp[0]
    
# Time Complexity: O(n) where n is the number of elements in the list.
# Space Complexity: O(1) since we are using a fixed-size array of length