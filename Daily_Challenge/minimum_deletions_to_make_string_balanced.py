#1653. Minimum Deletions to Make String Balanced

class Solution:
    def minimumDeletions(self, s: str) -> int:
        # dp stores the minimum deletions needed to balance the string processed so far
        dp = 0
        
        # count_b tracks the number of 'b's encountered so far
        count_b = 0
        
        for char in s:
            if char == 'b':
                # If we see a 'b', we just increment the count.
                # It doesn't immediately force a deletion in a valid prefix.
                count_b += 1
            else:
                # If we see an 'a', we have a potential conflict.
                # Option 1: Delete this 'a'. Cost = current dp + 1.
                # Option 2: Keep this 'a'. To do so, we must have deleted all previous 'b's. Cost = count_b.
                # We take the minimum of these two options.
                dp = min(dp + 1, count_b)
                
        return dp
    
# Time Complexity: O(n) - We traverse the string once, where n is the length of the string.
# Space Complexity: O(1) - We are using only a constant amount of extra space for the dp and count_b variables.