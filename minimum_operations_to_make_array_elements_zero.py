#3495. Minimum Operations to Make Array Elements Zero

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def depth(x):
            k = 0
            n = x
            while n:
                k += 1
                n //= 4
            return k
        
        segments = []
        base = 1
        for k in range(1, 17):
            low_seg = base
            high_seg = base * 4 - 1
            segments.append((low_seg, high_seg, k))
            base *= 4
        
        total_ops = 0
        for l, r in queries:
            total_depth = 0
            for low, high, k in segments:
                if low > r:
                    break
                if high < l:
                    continue
                low_actual = max(l, low)
                high_actual = min(r, high)
                if low_actual <= high_actual:
                    count = high_actual - low_actual + 1
                    total_depth += k * count
            M = depth(r)
            ops = max(M, (total_depth + 1) // 2)
            total_ops += ops
            
        return total_ops

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the number of queries.