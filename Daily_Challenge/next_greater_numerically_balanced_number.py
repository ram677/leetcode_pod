#2048. Next Greater Numerically Balanced Number

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:    
        # Start checking from the number right after n.
        num = n + 1
        
        while True:
            if self.is_numerically_balanced(num):
                return num
            num += 1

    def is_numerically_balanced(self, x: int) -> bool:
        # Count the occurrences of each digit in the number.
        counts = [0] * 10
        s = str(x)
        for char_digit in s:
            counts[int(char_digit)] += 1
        
        # Verify the balanced condition for each digit present in the number.
        for char_digit in s:
            digit = int(char_digit)
            # The count of the digit must match the digit's value.
            if counts[digit] != digit:
                return False
                
        # If all checks pass, the number is balanced.
        return True

#Time Complexity: O(m * d) where m is the number of integers checked after n and d is the number of digits in each integer.
#Space Complexity: O(1) since the counts array has a fixed size of 10.