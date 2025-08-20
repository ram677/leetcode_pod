#1277. Count Square Submatrices with All Ones

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    total += dp[i][j]
        
        return total

#Time Complexity: O(m * n)
#Space Complexity: O(m * n)
#Where m is the number of rows and n is the number of columns in the matrix.