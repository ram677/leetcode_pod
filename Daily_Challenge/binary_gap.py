#868. Binary Gap

class Solution:
    def binaryGap(self, n: int) -> int:
        last_pos = -1
        max_dist = 0
        pos = 0
        
        while n > 0:
            # Check if the current least significant bit is 1
            if n & 1:
                if last_pos != -1:
                    # Calculate distance and update max_dist
                    max_dist = max(max_dist, pos - last_pos)
                
                # Update the position of the last seen 1
                last_pos = pos
                
            # Shift right to process the next bit and increment position
            n >>= 1
            pos += 1
            
        return max_dist

# Time Complexity: O(log N) where N is the input number, since we are processing each bit.
# Space Complexity: O(1) since we are using a constant amount of space for variables.