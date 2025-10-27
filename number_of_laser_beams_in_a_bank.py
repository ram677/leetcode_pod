#2125. Number of Laser Beams in a Bank

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        prev_row_devices = 0
        
        # Iterate through each row of the bank floor plan.
        for row in bank:
            # Count the number of security devices ('1's) in the current row.
            current_row_devices = row.count('1')
            
            # If the current row is empty, it doesn't affect the beams, so we skip it.
            if current_row_devices == 0:
                continue
            
            # If the current row has devices, they form beams with the previous non-empty row.
            # The number of beams is the product of the device counts in the two rows.
            total_beams += prev_row_devices * current_row_devices
            
            # Update the previous device count to the current one for the next non-empty row.
            prev_row_devices = current_row_devices
            
        return total_beams
    
#Time Complexity:
# The solution iterates through each row of the bank once, and counting '1's in each row takes O(m) time where m is the number of columns.
# Therefore, the overall time complexity is O(n * m), where n is the number of rows.
#Space Complexity: O(1) since we are using a constant amount of extra space.