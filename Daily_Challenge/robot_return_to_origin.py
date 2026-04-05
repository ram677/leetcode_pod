#657. Robot Return to Origin

class Solution:
  def judgeCircle(self, moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')

# Time Complexity: O(n), where n is the length of the input string moves.
# Space Complexity: O(1), since we are using a constant amount of space to store the counts of moves.