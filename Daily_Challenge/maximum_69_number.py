#1323. Maximum 69 Number

class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert number to string for easy manipulation
        num_str = list(str(num))
        
        # Find the first 6 and change it to 9
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break   # only change the first one
        
        # Convert back to integer
        return int("".join(num_str))

#Time Complexity: O(n), where n is the number of digits in the input number.
#Space Complexity: O(n), for storing the string representation of the number.