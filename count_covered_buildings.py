#3531. Count Covered Buildings

class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        # Dictionaries to store the min and max coordinates for rows and columns
        # row_ranges[y] = [min_x, max_x]
        row_ranges = {}
        # col_ranges[x] = [min_y, max_y]
        col_ranges = {}
        
        # Pass 1: Populate min/max for each row and column
        for x, y in buildings:
            # Update row ranges (fixed y, varying x)
            if y not in row_ranges:
                row_ranges[y] = [x, x]
            else:
                if x < row_ranges[y][0]:
                    row_ranges[y][0] = x
                if x > row_ranges[y][1]:
                    row_ranges[y][1] = x
            
            # Update column ranges (fixed x, varying y)
            if x not in col_ranges:
                col_ranges[x] = [y, y]
            else:
                if y < col_ranges[x][0]:
                    col_ranges[x][0] = y
                if y > col_ranges[x][1]:
                    col_ranges[x][1] = y
                    
        count = 0
        
        # Pass 2: Check conditions for each building
        for x, y in buildings:
            # Check horizontal neighbors (Left and Right)
            # Must be strictly between the min x and max x in this row
            has_horizontal = row_ranges[y][0] < x < row_ranges[y][1]
            
            # Check vertical neighbors (Below and Above)
            # Must be strictly between the min y and max y in this column
            has_vertical = col_ranges[x][0] < y < col_ranges[x][1]
            
            if has_horizontal and has_vertical:
                count += 1
                
        return count
    
# Time Complexity: O(n), where n is the number of buildings.
# Space Complexity: O(n), for storing the row and column ranges.