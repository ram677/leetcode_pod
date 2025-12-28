#3000. Maximum Area of Longest Diagonal Rectangle

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        Finds the area of the rectangle with the longest diagonal.
        In case of a tie in diagonal length, the one with the maximum area is chosen.
        """
        max_diag_sq = 0
        max_area = 0

        for length, width in dimensions:
            # Calculate the squared diagonal length to avoid sqrt()
            current_diag_sq = length**2 + width**2
            
            # If the current diagonal is longer, this is the new best rectangle
            if current_diag_sq > max_diag_sq:
                max_diag_sq = current_diag_sq
                max_area = length * width
            # If the diagonals are equal, check if the area is larger
            elif current_diag_sq == max_diag_sq:
                max_area = max(max_area, length * width)
                
        return max_area

#Time Complexity: O(n), where n is the number of rectangles
#Space Complexity: O(1), as we are using only a constant amount of extra space