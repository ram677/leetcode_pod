#1536. Minimum Swaps to Arrange a Binary Grid

class Solution:
  def minSwaps(self, grid: list[list[int]]) -> int:
    n = len(grid)
    ans = 0
    # suffixZeros[i] := the number of suffix zeros in the i-th row
    suffixZeros = [n if 1 not in row else row[::-1].index(1) for row in grid]

    for i in range(n):
      neededZeros = n - 1 - i
      # Get the first row with suffix zeros >= `neededZeros` in suffixZeros[i:..n).
      j = next((j for j in range(i, n) if suffixZeros[j] >= neededZeros), -1)
      if j == -1:
        return -1
      # Move the rows[j] to the rows[i].
      for k in range(j, i, -1):
        suffixZeros[k] = suffixZeros[k - 1]
      ans += j - i

    return ans

# Time Complexity: O(n^2), where n is the number of rows (or columns) in the grid. We iterate through each row and for each row, we may need to check subsequent rows to find a suitable one.
# Space Complexity: O(n), where n is the number of rows in the grid. We use an additional list `suffixZeros` to store the number of suffix zeros for each row.