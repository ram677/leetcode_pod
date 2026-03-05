#1758. Minimum Changes To Make Alternating Binary String

class Solution:
  def minOperations(self, s: str) -> int:
    # the cost to make s "1010"
    cost10 = sum(int(c) == i % 2 for i, c in enumerate(s))
    # the cost to make s "0101"
    cost01 = len(s) - cost10
    return min(cost10, cost01)
  
# Time Complexity: O(n), where n is the length of the input string s. We need to iterate through all characters of the string to calculate the cost of making it "1010" and "0101".
# Space Complexity: O(1), as we are using only a constant amount of extra space to store the costs and the final answer.