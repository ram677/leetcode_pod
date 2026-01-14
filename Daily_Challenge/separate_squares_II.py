#3454. Separate Squares II

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # --- Step 1: Coordinate Compression for X-axis ---
        # We need to map large X coordinates to small indices for the Segment Tree.
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        
        # Sorted unique X coordinates define the "elementary intervals"
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        m = len(sorted_x) - 1  # Number of elementary intervals
        
        # --- Step 2: Create Vertical Sweep Events ---
        # Events: (y, type, x_start_idx, x_end_idx)
        # type 1: Square starts (bottom edge)
        # type -1: Square ends (top edge)
        events = []
        for x, y, l in squares:
            events.append((y, 1, x_map[x], x_map[x+l]))
            events.append((y + l, -1, x_map[x], x_map[x+l]))
            
        # Sort events by Y coordinate to process from bottom to top
        events.sort(key=lambda e: e[0])
        
        # --- Step 3: Segment Tree Initialization ---
        # count: number of active squares fully covering a node's range
        # total_len: the length of the union of intervals within a node's range
        count = [0] * (4 * m)
        total_len = [0.0] * (4 * m)
        
        def update(node, start, end, l, r, val):
            # Standard Segment Tree range update
            if l >= end or r <= start:
                return
            
            if l <= start and end <= r:
                count[node] += val
            else:
                mid = (start + end) // 2
                update(2 * node, start, mid, l, r, val)
                update(2 * node + 1, mid, end, l, r, val)
            
            # Update the 'covered length' for this node
            if count[node] > 0:
                # If fully covered by at least one square, the length is the full width of this range
                total_len[node] = sorted_x[end] - sorted_x[start]
            elif end - start == 1:
                # Leaf node with no coverage
                total_len[node] = 0
            else:
                # Internal node with no full coverage: sum of children
                total_len[node] = total_len[2 * node] + total_len[2 * node + 1]

        # --- Step 4: First Sweep - Calculate Strip Areas ---
        strips = [] # Store (height, active_width, y_start)
        prev_y = events[0][0]
        
        for y, type, x_start, x_end in events:
            height = y - prev_y
            
            if height > 0:
                # The 'total_len[1]' (root of tree) gives the total width of the union of active squares
                strips.append((height, total_len[1], prev_y))
            
            # Update the active intervals for the current y-coordinate
            update(1, 0, m, x_start, x_end, type)
            prev_y = y
            
        # --- Step 5: Second Sweep - Find the Split Line ---
        total_area = sum(h * w for h, w, _ in strips)
        target = total_area / 2.0
        
        current_area = 0.0
        for h, w, y_start in strips:
            segment_area = h * w
            if current_area + segment_area >= target:
                # The target dividing line is inside this strip
                if w == 0: return float(y_start)
                needed = target - current_area
                return y_start + (needed / w)
            current_area += segment_area
            
        return float(prev_y)
    
# Time Complexity: O(N log N) due to sorting and segment tree operations, where N is the number of squares.
# Space Complexity: O(N) for storing events and segment tree data.