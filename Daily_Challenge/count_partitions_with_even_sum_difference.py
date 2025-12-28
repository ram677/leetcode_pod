#3432. Count Partitions with Even Sum Difference

class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        count = 0
        
        # Iterate through possible partition points.
        # A partition at index i includes nums[i] in the left part.
        # Valid indices for i are 0 to n-2 (leaving at least one element for the right).
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            
            if (left_sum - right_sum) % 2 == 0:
                count += 1
                
        return count
    
#Time Complexity: O(n), where n is the length of the input list.
#Space Complexity: O(1), since we are using a constant amount of extra space.