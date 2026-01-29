#2976. Minimum Cost to Convert String I

from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize a 26x26 matrix with infinity to represent the cost between characters.
        # 0 corresponds to 'a', 1 to 'b', ..., 25 to 'z'.
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        # The cost to convert a character to itself is always 0.
        for i in range(26):
            dist[i][i] = 0
            
        # Populate the initial costs from the input arrays.
        # We use min() because there might be multiple entries for the same pair,
        # and we only care about the cheapest direct edge.
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
            
        # Floyd-Warshall Algorithm to find all-pairs shortest paths.
        # We try to use every character 'k' as an intermediate step between 'i' and 'j'.
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    # If going from i -> k -> j is cheaper than the current known path i -> j, update it.
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        
        total_cost = 0
        
        # Iterate through the source and target strings to calculate total cost.
        for s, t in zip(source, target):
            if s == t:
                continue
            
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            
            # If the cost is still infinity, conversion is impossible.
            if dist[u][v] == inf:
                return -1
            
            total_cost += dist[u][v]
            
        return total_cost
    
# Time Complexity: O(26^3 + n) where n is the length of the source/target strings.
# Space Complexity: O(26^2) for the distance matrix.