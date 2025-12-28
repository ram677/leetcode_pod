#2221. Find Triangular Sum of an Array

from typing import List

class Solution:
  def triangularSum(self, nums: List[int]) -> int:
    # Get the current number of elements.
    n = len(nums)
    
    # The process continues until only one element is left.
    # This will take n - 1 rounds of reduction.
    while n > 1:
      # Create a new list for the next row of the "triangle".
      new_nums = []
      
      # Calculate the elements of the new row.
      for i in range(n - 1):
        # The value is the sum of adjacent elements modulo 10.
        new_element = (nums[i] + nums[i+1]) % 10
        new_nums.append(new_element)
      
      # Replace the old list with the newly computed one.
      nums = new_nums
      # Update the length for the next iteration.
      n -= 1
      
    # When the loop finishes, nums contains the single remaining element.
    return nums[0]
  
# Time Complexity: O(n^2) because we perform n-1 rounds, and each round involves summing up to n elements.
# Space Complexity: O(n) for storing the intermediate rows.