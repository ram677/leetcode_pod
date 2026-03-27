#2946. Matrix Similarity After Cyclic Shifts

class Solution:
  def areSimilar(self, mat: list[list[int]], k: int) -> bool:
    n = len(mat[0])
    for row in mat:
      for j in range(n):
        if row[j] != row[(j + k) % n]:
          return False
    return True
  
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the matrix, since we need to check each element in the matrix.        
# Space Complexity: O(1) since we are using only a constant amount of extra space for variables.