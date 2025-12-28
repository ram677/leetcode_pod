#611. Valid Triangle Number

from typing import List

class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    n = len(nums)
    # A triangle requires at least 3 sides.
    if n < 3:
      return 0
    
    # Sort the array to efficiently apply the triangle inequality theorem.
    nums.sort()
    
    count = 0
    
    # Fix the longest side 'c' (nums[k]) and find pairs (a, b) such that a + b > c.
    # We iterate 'k' from the end of the array down to index 2.
    for k in range(n - 1, 1, -1):
      # Use two pointers for the other two sides 'a' (nums[left]) and 'b' (nums[right]).
      left, right = 0, k - 1
      
      while left < right:
        # Check if the triangle inequality holds (a + b > c).
        if nums[left] + nums[right] > nums[k]:
          # If nums[left] + nums[right] > nums[k], then for the current 'right',
          # all elements from 'left' to 'right - 1' will also form a valid
          # triangle with nums[right] and nums[k].
          # The number of such valid pairs is (right - left).
          count += (right - left)
          
          # We've counted all valid 'a's for this 'b', so try a smaller 'b'.
          right -= 1
        else:
          # The sum is too small, so we need a larger 'a'.
          left += 1
          
    return count
  
# Time Complexity: O(n^2) where n is the length of nums.
# Space Complexity: O(1) if we ignore the space used for sorting (which is O(n) in the worst case).