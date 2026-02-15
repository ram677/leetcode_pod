#67. Add Binary

# Approach 1:Simulation
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # 1 + 1 = 2 (binary 10), so carry is 1, digit is 0
            # 1 + 0 = 1 (binary 01), so carry is 0, digit is 1
            carry = total // 2
            res.append(str(total % 2))
            
        return "".join(res[::-1])
    
# Time Complexity: O(max(len(a), len(b))) since we process each digit of the longer string, where len(a) and len(b) are the lengths of the input binary strings.
# Space Complexity: O(max(len(a), len(b))) for the result string, which in the worst case can be one digit longer than the longer input string due to carry.

# Approach 2: Native Conversion

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary strings to integers, add them, and convert back to binary
        # bin() returns string like "0b101", so slice off the first two chars
        return bin(int(a, 2) + int(b, 2))[2:]
    

# Time Complexity: O(max(len(a), len(b))) for the conversion of binary strings to integers and back, where len(a) and len(b) are the lengths of the input binary strings.
# Space Complexity: O(max(len(a), len(b))) for the result string, which in the worst case can be one digit longer than the longer input string due to carry.