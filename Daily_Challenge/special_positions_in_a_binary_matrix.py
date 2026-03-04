#1582. Special Positions in a Binary Matrix

class Solution:
  def numSpecial(self, mat: list[list[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    ans = 0
    rowOnes = [0] * m
    colOnes = [0] * n

    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1:
          rowOnes[i] += 1
          colOnes[j] += 1

    for i in range(m):
      for j in range(n):
        if mat[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1:
          ans += 1

    return ans

# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the input matrix. We need to iterate through all elements of the matrix to count the number of ones in each row and column, and then iterate again to count the special positions.
# Space Complexity: O(m + n), where m is the number of rows and n is the number of columns in the input matrix. We use two additional arrays to store the count of ones in each row and column, which requires O(m) and O(n) space respectively.