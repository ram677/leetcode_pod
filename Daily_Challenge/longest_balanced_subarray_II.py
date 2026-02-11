#3721. Longest Balanced Subarray II

import sys

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Segment Tree Arrays
        # We need min and max to check for the existence of 0 in a range
        self.tree_min = [float('inf')] * (4 * n)
        self.tree_max = [float('-inf')] * (4 * n)
        self.lazy = [0] * (4 * n)
        
        last_pos = {}
        max_len = 0
        
        for j in range(n):
            num = nums[j]
            prev = last_pos.get(num, -1)
            
            # 1. Activate the current index j with base value 0
            # Effectively, before adding nums[j], the "subarray" starting at j 
            # (which would be empty) has a diff of 0. 
            # We do a point update to set index j to 0.
            self.point_update(1, 0, n - 1, j, 0)
            
            # 2. Update the range (prev + 1, j)
            # If num is even, it adds +1 to distinct evens count
            # If num is odd, it adds -1 (conceptually distinct odds count)
            # This affects all subarrays starting after the previous occurrence of num
            val = 1 if num % 2 == 0 else -1
            self.range_update(1, 0, n - 1, prev + 1, j, val)
            
            # 3. Query for the leftmost index i where value is 0
            idx = self.query_first_zero(1, 0, n - 1, 0, j)
            
            if idx != -1:
                max_len = max(max_len, j - idx + 1)
            
            last_pos[num] = j
            
        return max_len

    def push(self, node):
        if self.lazy[node] != 0:
            lz = self.lazy[node]
            # Apply to left child
            self.tree_min[2 * node] += lz
            self.tree_max[2 * node] += lz
            self.lazy[2 * node] += lz
            
            # Apply to right child
            self.tree_min[2 * node + 1] += lz
            self.tree_max[2 * node + 1] += lz
            self.lazy[2 * node + 1] += lz
            
            # Reset current
            self.lazy[node] = 0

    def point_update(self, node, start, end, idx, val):
        if start == end:
            self.tree_min[node] = val
            self.tree_max[node] = val
            self.lazy[node] = 0
            return
        
        self.push(node)
        mid = (start + end) // 2
        if idx <= mid:
            self.point_update(2 * node, start, mid, idx, val)
        else:
            self.point_update(2 * node + 1, mid + 1, end, idx, val)
            
        self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])
        self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])

    def range_update(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            self.tree_min[node] += val
            self.tree_max[node] += val
            self.lazy[node] += val
            return
            
        self.push(node)
        mid = (start + end) // 2
        self.range_update(2 * node, start, mid, l, r, val)
        self.range_update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])
        self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])

    def query_first_zero(self, node, start, end, l, r):
        # If range is invalid or 0 is impossible in this range (min > 0 or max < 0)
        # Note: Since the counts change by +/- 1 steps, Intermediate Value Theorem applies.
        # If min <= 0 <= max, a 0 exists.
        if l > end or r < start or self.tree_min[node] > 0 or self.tree_max[node] < 0:
            return -1
        
        if start == end:
            return start if self.tree_min[node] == 0 else -1
        
        self.push(node)
        mid = (start + end) // 2
        
        # Try left child first to find the leftmost (longest subarray)
        res = self.query_first_zero(2 * node, start, mid, l, r)
        if res != -1:
            return res
            
        return self.query_first_zero(2 * node + 1, mid + 1, end, l, r)
    
# Time Complexity: O(n log n) - Each of the n elements is processed with segment tree updates and queries.
# Space Complexity: O(n) - The segment tree and lazy arrays take O(n) space.