# 3479. Fruits Into Baskets III

import sys

sys.setrecursionlimit(200000)

class Solution:
  def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
    n = len(fruits)
    tree = [0] * (4 * n)
    
    def build(node: int, start: int, end: int):
      if start == end:
        tree[node] = baskets[start]
        return
      mid = (start + end) // 2
      build(2 * node + 1, start, mid)
      build(2 * node + 2, mid + 1, end)
      tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

    def query(node: int, start: int, end: int, val: int) -> int:
      if tree[node] < val:
        return -1
      
      if start == end:
        return start
      
      mid = (start + end) // 2
      
      if tree[2 * node + 1] >= val:
        return query(2 * node + 1, start, mid, val)
      
      return query(2 * node + 2, mid + 1, end, val)

    def update(node: int, start: int, end: int, idx: int, new_val: int):
      if start == end:
        tree[node] = new_val
        return

      mid = (start + end) // 2
      if start <= idx <= mid:
        update(2 * node + 1, start, mid, idx, new_val)
      else:
        update(2 * node + 2, mid + 1, end, idx, new_val)
      
      tree[node] = max(tree[2 * node + 1], tree[2 * node + 2])

    if n > 0:
        build(0, 0, n - 1)
    
    unplaced_count = 0
    for fruit in fruits:
      basket_idx = -1
      if n > 0:
        basket_idx = query(0, 0, n - 1, fruit)
      
      if basket_idx == -1:
        unplaced_count += 1
      else:
        update(0, 0, n - 1, basket_idx, -1)
            
    return unplaced_count

# Time Complexity: O(nlogn) for building the segment tree and O(logn) for each query and update, leading to O(nlogn) overall.
# Space Complexity: O(n) for the segment tree.
# Note: The solution assumes that the input lists 'fruits' and 'baskets' are non-empty and contain valid integers.