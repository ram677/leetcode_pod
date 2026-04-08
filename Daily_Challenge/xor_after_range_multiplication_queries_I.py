#3653. XOR After Range Multiplication Queries I

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        for l, r, k, v in queries:
            for idx in range(l, r + 1, k):
                nums[idx] = nums[idx] * v % mod
        return reduce(xor, nums)

# Time Complexity: O(n * m / k), where n is the length of nums, m is the number of queries, and k is the step size in the queries. In the worst case, if k = 1, the time complexity would be O(n * m).
# Space Complexity: O(1) if we ignore the space used for the input and output, since we are modifying the nums list in place and using a constant amount of extra space for the XOR operation.