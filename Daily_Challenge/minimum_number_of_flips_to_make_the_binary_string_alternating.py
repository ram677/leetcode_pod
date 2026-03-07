#1888. Minimum Number of Flips to Make the Binary String Alternating

class Solution:
  def minFlips(self, s: str) -> int:
    n = len(s)
    # count[0][0] :=  the number of '0' in the even indices
    # count[0][1] :=  the number of '0' in the odd indices
    # count[1][0] :=  the number of '1' in the even indices
    # count[1][1] :=  the number of '1' in the odd indices
    count = [[0] * 2 for _ in range(2)]

    for i, c in enumerate(s):
      count[int(c)][i % 2] += 1

    # min(make all 0s in the even indices + make all 1s in the odd indices,
    #     make all 1s in the even indices + make all 0s in the odd indices)
    ans = min(count[1][0] + count[0][1], count[0][0] + count[1][1])

    for i, c in enumerate(s):
      count[int(c)][i % 2] -= 1
      count[int(c)][(n + i) % 2] += 1
      ans = min(ans, count[1][0] + count[0][1], count[0][0] + count[1][1])

    return ans

# Time Complexity: O(n), where n is the length of the input string s. We need to iterate through the string twice, which takes O(n) time.
# Space Complexity: O(1), as we are using only a constant amount of extra space to store the count of characters in even and odd indices.