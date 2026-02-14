#799. Champagne Tower

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a 2D array to store the amount of liquid in each glass.
        # Max row is 99, so a size of 102x102 is safe to handle the overflow to the next row.
        dp = [[0.0] * 102 for _ in range(102)]
        
        # Pour all champagne into the top glass
        dp[0][0] = poured
        
        # Process each row to distribute the overflow to the next row
        # We only need to process up to query_row - 1 to fill query_row
        for r in range(query_row):
            for c in range(r + 1):
                # Calculate the excess liquid
                excess = (dp[r][c] - 1.0) / 2.0
                
                # If there is excess, distribute it equally to the children glasses
                if excess > 0:
                    dp[r+1][c] += excess
                    dp[r+1][c+1] += excess
        
        # The glass holds at most 1 cup; any remaining excess spills over to the floor
        # (or the next row, which we don't care about for the final answer).
        return min(1.0, dp[query_row][query_glass])
    
# Time Complexity: O(query_row^2) since we process each row up to query_row and each row has at most r+1 glasses.
# Space Complexity: O(1) since we are using a fixed-size 2D array to store the amounts, which does not grow with input size.