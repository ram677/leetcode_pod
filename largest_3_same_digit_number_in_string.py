#2264. Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:  # all digits same
                if sub > max_good:
                    max_good = sub
        return max_good

#Time Complexity: O(n), where n is the length of the input string.
#Space Complexity: O(1), since we are using a constant amount of space.