#1545. Find Kth Bit in Nth Binary String

class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    if n == 1:
      return '0'
    midIndex = pow(2, n - 1)  # 1-indexed
    if k == midIndex:
      return '1'
    if k < midIndex:
      return self.findKthBit(n - 1, k)
    return '1' if self.findKthBit(n - 1, midIndex * 2 - k) == '0' else '0'
  
# Time Complexity: O(n), where n is the input integer. In the worst case, we may need to recursively call the function n times until we reach the base case.
# Space Complexity: O(n), where n is the input integer. The space complexity is due to the recursive call stack, which can go up to n levels deep in the worst case.