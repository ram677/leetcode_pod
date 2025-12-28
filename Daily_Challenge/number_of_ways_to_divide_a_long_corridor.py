#2147. Number of Ways to Divide a Long Corridor

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Collect indices of all seats
        seats = [i for i, char in enumerate(corridor) if char == 'S']
        
        # Step 2: Validate seat count
        # Must have at least 2 seats, and total count must be even
        if not seats or len(seats) % 2 != 0:
            return 0
        
        # Step 3: Calculate the product of gaps between pairs
        ways = 1
        
        # We iterate starting from the gap between the first pair (indices 0, 1)
        # and the second pair (indices 2, 3).
        # The relevant gap is between seats[1] and seats[2], then seats[3] and seats[4], etc.
        for i in range(2, len(seats), 2):
            prev_end = seats[i - 1]
            next_start = seats[i]
            
            # The number of ways to place a divider between these two seats
            # is the distance between their indices.
            gap_ways = next_start - prev_end
            
            ways = (ways * gap_ways) % MOD
            
        return ways
    
# Time Complexity: O(n), where n is the length of the corridor string.
# Space Complexity: O(m), where m is the number of seats in the corridor.