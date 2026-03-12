#3600. Maximize Spanning Tree Stability with Upgrades

from typing import List

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        class DSU:
            def __init__(self, n, parent=None, rank=None, components=None):
                if parent is None:
                    self.parent = list(range(n))
                    self.rank = [1] * n
                    self.components = n
                else:
                    self.parent = parent[:]
                    self.rank = rank[:]
                    self.components = components

            def find(self, i):
                if self.parent[i] == i:
                    return i
                curr = i
                path = []
                while self.parent[curr] != curr:
                    path.append(curr)
                    curr = self.parent[curr]
                for node in path:
                    self.parent[node] = curr
                return curr

            def union(self, i, j):
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i != root_j:
                    if self.rank[root_i] < self.rank[root_j]:
                        self.parent[root_i] = root_j
                    elif self.rank[root_i] > self.rank[root_j]:
                        self.parent[root_j] = root_i
                    else:
                        self.parent[root_j] = root_i
                        self.rank[root_i] += 1
                    self.components -= 1
                    return True
                return False

        mandatory_edges = []
        optional_edges = []
        min_mandatory = float('inf')
        
        for u, v, s, must in edges:
            if must:
                mandatory_edges.append((u, v, s))
                if s < min_mandatory:
                    min_mandatory = s
            else:
                optional_edges.append((u, v, s))
                
        test_dsu = DSU(n)
        for u, v, s in mandatory_edges:
            test_dsu.union(u, v)
        for u, v, s in optional_edges:
            test_dsu.union(u, v)
        if test_dsu.components > 1:
            return -1
            
        base_dsu = DSU(n)
        for u, v, s in mandatory_edges:
            if not base_dsu.union(u, v):
                return -1 
                
        vals = set()
        for u, v, s in mandatory_edges:
            if s <= min_mandatory:
                vals.add(s)
        for u, v, s in optional_edges:
            if s <= min_mandatory:
                vals.add(s)
            if s * 2 <= min_mandatory:
                vals.add(s * 2)
                
        if not vals:
            return -1
            
        vals = sorted(list(vals))
        
        def can_form(X):
            dsu = DSU(n, base_dsu.parent, base_dsu.rank, base_dsu.components)
            
            for u, v, s in optional_edges:
                if s >= X:
                    dsu.union(u, v)
                    
            if dsu.components == 1:
                return True
                
            upgrades = 0
            for u, v, s in optional_edges:
                if s < X and s * 2 >= X:
                    if dsu.union(u, v):
                        upgrades += 1
                        if dsu.components == 1:
                            return upgrades <= k
            return False

        ans = -1
        low = 0
        high = len(vals) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form(vals[mid]):
                ans = vals[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
    
# Time Complexity: O(E log E + E log V), where E is the number of edges and V is the number of vertices. Sorting the edges takes O(E log E) time, and the binary search involves O(log E) iterations, each requiring O(E log V) time for the union-find operations.
# Space Complexity: O(V + E), where V is the number of vertices and E is the number of edges. The union-find data structure requires O(V) space, and we also store the edges in separate lists, which takes O(E) space.