# 3479. Fruits Into Baskets III

import collections

class Solution:
  def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
    n = len(fruits)
    available = [True] * n
    unplaced_count = 0
    
    for fruit in fruits:
      placed = False
      for i in range(n):
        if available[i] and baskets[i] >= fruit:
          available[i] = False
          placed = True
          break
      
      if not placed:
        unplaced_count += 1
        
    return unplaced_count

# Time Complexity: O(n^2), where n is the length of fruits 
# Space Complexity: O(n), for the available list to track basket usage.