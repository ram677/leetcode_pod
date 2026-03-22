#1886. Determine Whether Matrix Can Be Obtained By Rotation

class Solution:
  def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
    for _ in range(4):
      if mat == target:
        return True
      mat = [list(x) for x in zip(*mat[::-1])]
    return False
  
# Time Complexity: O(1) since the size of the matrix is fixed at 3x3.
# Space Complexity: O(1) since we are modifying the matrix in place and not using any additional data structures that grow with input size.