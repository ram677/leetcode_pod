#1518. Water Bottles

class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    # Initially, you drink all the bottles you have.
    total_drunk = numBottles
    empty_bottles = numBottles
    
    # Continue the process as long as you can exchange empty bottles for full ones.
    while empty_bottles >= numExchange:
      # Perform the exchange.
      new_full_bottles = empty_bottles // numExchange
      remaining_empty = empty_bottles % numExchange
      
      # Drink the newly acquired bottles.
      total_drunk += new_full_bottles
      
      # Update the number of empty bottles you now have.
      # It's the leftovers from the exchange plus the ones you just drank.
      empty_bottles = remaining_empty + new_full_bottles
      
    return total_drunk
  
# Time Complexity: O(log n) because the number of bottles decreases logarithmically with each exchange.
# Space Complexity: O(1) since we are using a constant amount of extra space.