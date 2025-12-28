# 3542. Minimum Operations to Convert All Elements to Zero

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        operations = 0
        for num in nums:
            if num == 0:
                operations += len(stack)
                stack = []
                continue
            while stack and stack[-1] > num:
                stack.pop()
                operations += 1
            if stack and stack[-1] == num:
                continue
            else:
                stack.append(num)
        operations += len(stack)
        return operations
    
# Time Complexity: O(n), where n is the number of elements in the input list.
# Space Complexity: O(n) in the worst case for the stack.