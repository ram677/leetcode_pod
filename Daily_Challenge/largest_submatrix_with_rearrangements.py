#1727. Largest Submatrix With Rearrangements

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        # Step 1: Calculate the height of consecutive 1s for each column
        for i in range(1, m):
            for j in range(n):
                # If the current cell is 1, add the height from the row above
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
                    
        # Step 2: Sort each row and calculate the maximum bounding rectangle
        for i in range(m):
            # Sort the heights in the current row in descending order
            curr_row = sorted(matrix[i], reverse=True)
            
            # Check the maximum area we can form using the sorted heights
            for j in range(n):
                # The height is determined by the current column (the shortest in our selection)
                # The width is j + 1 (since we are taking all columns from 0 to j)
                area = curr_row[j] * (j + 1)
                max_area = max(max_area, area)
                
        return max_area
    
# Time Complexity: O(m * n log n) due to sorting each row, where m is the number of rows and n is the number of columns.
# Space Complexity: O(1) if we sort in place, otherwise O(n) for the temporary array used for sorting.