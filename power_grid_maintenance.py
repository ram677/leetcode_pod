#3607. Power Grid Maintenance

from typing import List, Dict, Set
from collections import defaultdict

class DSU:
    def __init__(self, n):
        # 1-based indexing
        self.parent = list(range(n + 1))
        
    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
        
    def union(self, x: int, y: int) -> bool:
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rooty] = rootx
            return True
        return False

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        # 1. Build the DSU from connections
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)
            
        # 2. Precompute the sorted list of stations for each grid
        component_stations = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            component_stations[root].append(i)
            
        # 3. Initialize state trackers
        # Maps root -> index in component_stations[root]
        smallest_online_idx = {root: 0 for root in component_stations}
        offline_stations = set()
        results = []

        # 4. Process all queries
        for query_type, x in queries:
            if query_type == 1:
                # Type 1: Maintenance Check
                if x not in offline_stations:
                    results.append(x)
                else:
                    root = dsu.find(x)
                    idx = smallest_online_idx[root]
                    
                    if idx == -1: # All stations in this grid are offline
                        results.append(-1)
                    else:
                        results.append(component_stations[root][idx])
            
            elif query_type == 2:
                # Type 2: Station goes offline
                if x in offline_stations:
                    continue # Already offline
                
                offline_stations.add(x)
                root = dsu.find(x)
                
                idx = smallest_online_idx[root]
                if idx == -1: # Grid already offline
                    continue
                    
                stations = component_stations[root]
                
                # If the station going offline *was* the smallest online,
                # we must find the new smallest online.
                if x == stations[idx]:
                    idx += 1
                    # Move the pointer to the next online station
                    while idx < len(stations) and stations[idx] in offline_stations:
                        idx += 1
                    
                    if idx == len(stations): # All stations in this grid are now offline
                        smallest_online_idx[root] = -1
                    else:
                        smallest_online_idx[root] = idx
                        
        return results
    
# Time Complexity: O((C + Q) * α(C)) where C is the number of stations, Q is the number of queries, and α is the inverse Ackermann function.
# Space Complexity: O(C) for DSU and component storage.