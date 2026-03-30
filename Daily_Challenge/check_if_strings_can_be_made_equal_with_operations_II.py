#2840. Check if Strings Can be Made Equal With Operations II

class Solution:
  def checkStrings(self, s1: str, s2: str) -> bool:
    count = [collections.Counter() for _ in range(2)]

    for i, (a, b) in enumerate(zip(s1, s2)):
      count[i % 2][a] += 1
      count[i % 2][b] -= 1

    return (all(freq == 0 for freq in count[0].values()) and
            all(freq == 0 for freq in count[1].values()))

# Time complexity: O(n) - We iterate through both strings once to count the characters.
# Space complexity: O(1) - The space used for the counters is constant, as there are only 26 lowercase English letters.