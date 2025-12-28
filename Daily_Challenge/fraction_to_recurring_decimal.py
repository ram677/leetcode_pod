#166. Fraction to Recurring Decimal

class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    # Trivial case: numerator is 0
    if numerator == 0:
      return "0"

    # Use a list of strings for efficient concatenation
    res = []
    
    # 1. Determine the sign. The result is negative if signs differ.
    # The expression `(numerator < 0) != (denominator < 0)` acts as an XOR.
    if (numerator < 0) != (denominator < 0):
      res.append("-")

    # 2. Use absolute values for the division logic
    n, d = abs(numerator), abs(denominator)

    # 3. Calculate and append the integer part
    res.append(str(n // d))
    remainder = n % d

    # 4. If there's no remainder, the result is an integer
    if remainder == 0:
      return "".join(res)

    # 5. Handle the fractional part
    res.append(".")
    
    # Use a dictionary to store remainders and the index where they appeared
    remainders_map = {}

    while remainder != 0:
      # If the current remainder has been seen before, we have a repeating cycle
      if remainder in remainders_map:
        # Get the index where the repeating part starts
        start_index = remainders_map[remainder]
        # Insert the opening parenthesis at that index
        res.insert(start_index, '(')
        # Append the closing parenthesis
        res.append(')')
        # The calculation is complete
        break
      
      # Store the current remainder and its position (current length of res)
      remainders_map[remainder] = len(res)
      
      # Perform one step of long division
      remainder *= 10
      res.append(str(remainder // d))
      remainder %= d

    return "".join(res)
  
# Time Complexity: O(n) where n is the number of digits in the fractional part before repetition.
# Space Complexity: O(n) for storing the result and the remainders map.