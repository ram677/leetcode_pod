#3100. Water Bottles II

class Solution:
  def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    # Initially, you drink all the bottles you have.
    bottles_drunk = numBottles
    empty_bottles = numBottles
    
    # Continue the process as long as you can exchange empty bottles for full ones.
    while empty_bottles >= numExchange:
      # Perform the exchange: give away 'numExchange' empty bottles.
      empty_bottles -= numExchange
      
      # The exchange rate increases for the next time.
      numExchange += 1
      
      # You receive one new full bottle and drink it immediately.
      bottles_drunk += 1
      
      # The bottle you just drank becomes an empty one.
      empty_bottles += 1
      
    return bottles_drunk
  
# Time Complexity: O(n) in the worst case, where n is the number of bottles, as we may need to perform multiple exchanges.
# Space Complexity: O(1) since we are using a constant amount of extra space.