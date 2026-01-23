#3510. Minimum Pair Removal to Sort Array II

import heapq
from typing import List

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None
        self.removed = False

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # 1. Build Doubly Linked List
        nodes = [Node(x, i) for i, x in enumerate(nums)]
        for i in range(n - 1):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]
            
        # 2. Initialize Inversion Count & Min-Heap
        inversions = 0
        pq = [] # Stores (sum, start_node_index)
        
        curr = nodes[0]
        while curr and curr.next:
            # Check inversion
            if curr.val > curr.next.val:
                inversions += 1
            
            # Add to heap
            current_sum = curr.val + curr.next.val
            heapq.heappush(pq, (current_sum, curr.idx))
            
            curr = curr.next
            
        if inversions == 0:
            return 0
            
        ops = 0
        
        # 3. Process Merges
        while inversions > 0 and pq:
            s, idx = heapq.heappop(pq)
            u = nodes[idx]
            
            # --- Validation Checks (Lazy Deletion) ---
            # 1. Is node removed? 2. Is it the tail? 3. Is the sum stale?
            if u.removed or u.next is None or (u.val + u.next.val != s):
                continue
                
            v = u.next
            prev_node = u.prev
            next_node = v.next
            
            # --- Step A: Remove Old Relationships from Inversion Count ---
            # Check left boundary (prev -> u)
            if prev_node and prev_node.val > u.val:
                inversions -= 1
            # Check internal (u -> v)
            if u.val > v.val:
                inversions -= 1
            # Check right boundary (v -> next)
            if next_node and v.val > next_node.val:
                inversions -= 1
                
            # --- Step B: Merge Nodes ---
            # Update u's value and link u to next_node, bypassing v
            u.val = u.val + v.val
            u.next = next_node
            if next_node:
                next_node.prev = u
            
            # Mark v as removed
            v.removed = True
            ops += 1
            
            # --- Step C: Add New Relationships to Inversion Count ---
            # Check new left boundary (prev -> new_u)
            if prev_node and prev_node.val > u.val:
                inversions += 1
            # Check new right boundary (new_u -> next)
            if next_node and u.val > next_node.val:
                inversions += 1
                
            # --- Step D: Push New Sums to Heap ---
            # New pair to the right
            if u.next:
                heapq.heappush(pq, (u.val + u.next.val, u.idx))
            
            # New pair to the left (prev needs to be updated with u's new value)
            if u.prev:
                heapq.heappush(pq, (u.prev.val + u.val, u.prev.idx))
                
        return ops
    
# Time Complexity: O(n log n) due to heap operations, where n is the number of elements in nums.
# Space Complexity: O(n) for the doubly linked list and heap storage.