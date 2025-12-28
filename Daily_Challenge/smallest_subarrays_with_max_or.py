from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last = [0] * 32  # To track the last index where each bit was seen
        
        for i in range(n - 1, -1, -1):
            # Update the last seen index for each bit set in nums[i]
            for b in range(32):
                if (nums[i] >> b) & 1:
                    last[b] = i
            
            # The rightmost index we need to include to cover all bits
            max_index = i
            for b in range(32):
                max_index = max(max_index, last[b])
            
            answer[i] = max_index - i + 1
        
        return answer

#Time Complexity: O(n * 32) = O(n)
#Space Complexity: O(32 + n) = O(n)
#n is the length of the input list nums, i.e., the number of elements in the array.