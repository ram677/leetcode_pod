#401. Binary Watch

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        
        # Iterate through all possible hours (0-11)
        for h in range(12):
            # Iterate through all possible minutes (0-59)
            for m in range(60):
                
                # Count the total number of set bits (LEDs on)
                # bin(5) is "0b101", count('1') returns 2
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    
                    # Format the time correctly
                    # Hours don't have leading zeros (e.g., "1" not "01")
                    # Minutes must have two digits (e.g., "05" not "5")
                    times.append(f"{h}:{m:02d}")
                    
        return times
    
# Time Complexity: O(1) since we are iterating through a fixed number of hours (12) and minutes (60), resulting in a constant number of iterations (720).
# Space Complexity: O(1) for the output list, as the maximum number of valid times is limited by the number of combinations of LEDs that can be turned on, which is also constant.