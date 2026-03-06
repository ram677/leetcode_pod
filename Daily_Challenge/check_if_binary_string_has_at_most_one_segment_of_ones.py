#1784. Check if Binary String Has at Most One Segment of Ones

class Solution:
  def checkOnesSegment(self, s: str) -> bool:
    return '01' not in s
  
# Time Complexity: O(n), where n is the length of the input string s. We need to check if the substring "01" is present in the string, which takes O(n) time.
# Space Complexity: O(1), as we are using only a constant amount of extra space to store the result of the check.