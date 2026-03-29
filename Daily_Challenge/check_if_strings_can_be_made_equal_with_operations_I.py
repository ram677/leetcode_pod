#2839. Check if Strings Can be Made Equal With Operations I

class Solution:
  def canBeEqual(self, s1: str, s2: str) -> bool:
    def swappedStrings(s: str) -> list[str]:
      chars = list(s)
      return [chars,
              ''.join([chars[2], chars[1], chars[0], chars[3]]),
              ''.join([chars[0], chars[3], chars[2], chars[1]]),
              ''.join([chars[2], chars[3], chars[0], chars[1]])]

    return any(a == b
               for a in swappedStrings(s1)
               for b in swappedStrings(s2))
  
# Time complexity: O(1) - The number of possible strings is constant (4 for each string, total 16 comparisons).
# Space complexity: O(1) - The space used for storing the swapped strings is constant (4 for each string).