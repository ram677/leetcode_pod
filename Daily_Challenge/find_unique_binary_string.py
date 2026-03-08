#1980. Find Unique Binary String

class Solution:
  def findDifferentBinaryString(self, nums: list[str]) -> str:
    bitSize = len(nums[0])
    maxNum = 1 << bitSize
    numsSet = {int(num, 2) for num in nums}

    for num in range(maxNum):
      if num not in numsSet:
        return f'{num:0>{bitSize}b}'
      
# Time Complexity: O(n), where n is the length of the input list nums. We need to iterate through the list to create the set of binary numbers, which takes O(n) time. Then we iterate through the range of possible binary numbers, which takes O(2^k) time, where k is the number of bits in the binary numbers. However, since k is a constant (the length of the binary strings), this part can be considered O(1). Therefore, the overall time complexity is O(n).
# Space Complexity: O(n), as we are using a set to store the binary numbers from the input list, which takes O(n) space in the worst case.