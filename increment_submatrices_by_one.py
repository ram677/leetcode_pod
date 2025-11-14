#2536. Increment Submatrices by One

from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Create a matrix of size (n + 1) x (n + 1) to handle boundary checks easily
        mat = [[0] * (n + 1) for _ in range(n + 1)]
        
        # 1. Apply the Difference Array logic for each query
        for r1, c1, r2, c2 in queries:
            mat[r1][c1] += 1
            mat[r1][c2 + 1] -= 1
            mat[r2 + 1][c1] -= 1
            mat[r2 + 1][c2 + 1] += 1
            
        # 2. Compute 2D Prefix Sums to get the final values
        
        # Pass 1: Accumulate row-wise (left to right)
        for r in range(n):
            for c in range(1, n):
                mat[r][c] += mat[r][c - 1]
                
        # Pass 2: Accumulate column-wise (top to bottom)
        for r in range(1, n):
            for c in range(n):
                mat[r][c] += mat[r - 1][c]
                
        # 3. Return the original n x n part of the matrix (discard the padding)
        # We iterate only up to n because the n+1th row/col were just for padding
        result = []
        for r in range(n):
            result.append(mat[r][:n])
            
        return result
    
# Time Complexity: O(n^2 + q), where n is the size of the matrix and q is the number of queries.
# Space Complexity: O(n^2) for the matrix storage.