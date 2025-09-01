#1792. Maximum Average Pass Ratio

from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        # Max-heap based on gain (Python heapq is min-heap, so store negative)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1  # assign one student
            heapq.heappush(heap, (-gain(p, t), p, t))
        
        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t
        
        return total / len(classes)

#Time Complexity: O((n + m) log n) where n is the number of classes and m is extraStudents
#Space Complexity: O(n) for the heap