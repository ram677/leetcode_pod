#3453. Separate Squares I

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Calculate the total area of all squares
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2.0
        
        # Create events: (y_coordinate, change_in_width)
        # We process squares vertically. 
        # At square's bottom (y), we add 'l' to the active width.
        # At square's top (y + l), we subtract 'l' from the active width.
        events = []
        for _, y, l in squares:
            events.append((y, l))
            events.append((y + l, -l))
            
        # Sort events by coordinate.
        # This allows us to "sweep" from the bottom up.
        events.sort(key=lambda x: x[0])
        
        current_area = 0.0
        current_width = 0
        prev_y = events[0][0]
        
        for y, width_diff in events:
            # Calculate the height of the current horizontal strip
            height = y - prev_y
            
            # Area of this strip = height * total width of squares in this strip
            segment_area = height * current_width
            
            # Check if including this strip pushes us past or to the target area
            if current_area + segment_area >= target:
                # The target line is inside this strip.
                # We need to find 'missing_height' such that:
                # current_area + (missing_height * current_width) == target
                if current_width == 0:
                    # This happens if we reach the target exactly at a gap between squares
                    return float(prev_y)
                
                missing_area = target - current_area
                return prev_y + (missing_area / current_width)
            
            # Update accumulators for the next iteration
            current_area += segment_area
            current_width += width_diff
            prev_y = y
            
        return float(prev_y)

# Time Complexity: O(N log N) due to sorting the events, where N is the number of squares.
# Space Complexity: O(N) for storing the events.