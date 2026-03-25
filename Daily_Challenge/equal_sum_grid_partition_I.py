#3546. Equal Sum Grid Partition I

class Solution:
  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
    totalSum = sum(map(sum, grid))

    def canPartition(grid: list[list[int]]) -> bool:
      runningSum = 0
      for row in grid:
        runningSum += sum(row)
        if runningSum * 2 == totalSum:
          return True
      return False

    return canPartition(grid) or canPartition(zip(*grid))
  
# Time Complexity: O(n*m) where n and m are the dimensions of the grid, since we need to calculate the total sum and check for partitions.
# Space Complexity: O(1) since we are using a constant amount of extra space for variables. The input grid is not modified, and we are not using any additional data structures that grow with the input size.