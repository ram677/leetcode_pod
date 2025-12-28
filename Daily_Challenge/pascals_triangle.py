#118. Pascal's Triangle

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            if row == 0:
                triangle.append([1])
            else:
                prev_row = triangle[-1]
                new_row = [1]
                for i in range(1, row):
                    new_row.append(prev_row[i - 1] + prev_row[i])
                new_row.append(1)
                triangle.append(new_row)

        return triangle

# Time Complexity: O(n²) (generating each row up to n elements)
# Space Complexity: O(n²) (storing the entire triangle)
# n = numRows is the number of rows to generate in Pascal's Triangle.
# Each row has up to n elements.