#3228. Maximum Number of Operations to Move Ones to the End

class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones_count = 0
        
        for i in range(len(s)):
            if s[i] == '1':
                ones_count += 1
            elif i > 0 and s[i-1] == '1':
                # We found a '0' and the previous char was '1'.
                # This is the start of a gap. All accumulated 1s can "jump" here.
                ans += ones_count
                
        return ans
    
# Time Complexity: O(n), where n is the length of the string s.
# Space Complexity: O(1) as we are using only a constant amount of extra space