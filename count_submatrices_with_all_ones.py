#1504. Count Submatrices With All Ones

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        result = 0

        for i in range(m):
            # Build histogram for current row
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] else 0

            # Count submatrices ending at row i
            stack = []
            sum_row = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    sum_row[j] = sum_row[prev_index] + heights[j] * (j - prev_index)
                else:
                    sum_row[j] = heights[j] * (j + 1)
                stack.append(j)
                result += sum_row[j]

        return result

#Time Complexity: O(m * n)
#Space Complexity: O(n)
#Where m is the number of rows and n is the number of columns in the matrix.