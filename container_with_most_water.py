#11. Container With Most Water

from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0

    while left < right:
      # Calculate the area of the container
      width = right - left
      current_height = min(height[left], height[right])
      current_area = width * current_height
      
      # Update the maximum area found so far
      max_area = max(max_area, current_area)
      
      # Move the pointer that points to the shorter line to
      # have a chance of finding a larger area.
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
            
    return max_area
  
# Time Complexity: O(n) where n is the number of elements in the height array.
# Space Complexity: O(1) as we are using only a constant amount of extra space.