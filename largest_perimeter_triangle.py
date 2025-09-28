#976. Largest Perimeter Triangle

from typing import List

class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    # Sort the array to easily access the largest numbers.
    nums.sort()
    n = len(nums)
    
    # Iterate backwards, considering the three largest available numbers at each step.
    # The loop runs as long as there are at least 3 elements to check.
    for i in range(n - 1, 1, -1):
      # Let the three sides be a, b, and c, where a <= b <= c.
      c = nums[i]
      b = nums[i - 1]
      a = nums[i - 2]
      
      # For a valid triangle, we only need to check if the sum of the two
      # smaller sides is greater than the largest side.
      if a + b > c:
        # Since the array is sorted, this is the first valid triangle we've
        # found, and it must have the largest possible perimeter.
        return a + b + c
        
    # If the loop completes, no three sides could form a triangle.
    return 0
  
# Time Complexity: O(n log n) due to the sorting step.
# Space Complexity: O(1) if the sorting is done in place, otherwise O(n).