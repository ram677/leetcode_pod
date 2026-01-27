#3650. Minimum Cost Path with Edge Reversals

import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph adjacency list
        # graph[u] will store tuples of (neighbor, weight)
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            # 1. Normal traversal: u -> v cost w
            graph[u].append((v, w))
            # 2. Switch traversal: v -> u cost 2 * w
            # This represents arriving at v, using the switch to reverse u->v, 
            # and traversing back to u immediately.
            graph[v].append((u, 2 * w))
            
        # Dijkstra's Algorithm
        # Priority Queue stores (current_cost, current_node)
        pq = [(0, 0)]
        
        # Array to track the minimum cost to reach each node
        # Initialize with infinity
        min_costs = [float('inf')] * n
        min_costs[0] = 0
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            
            # If we reached the target node, we return the cost.
            # Dijkstra guarantees this is the minimum cost.
            if u == n - 1:
                return current_cost
            
            # Optimization: If we found a shorter path to u already, skip
            if current_cost > min_costs[u]:
                continue
            
            # Explore neighbors
            for v, weight in graph[u]:
                if current_cost + weight < min_costs[v]:
                    min_costs[v] = current_cost + weight
                    heapq.heappush(pq, (min_costs[v], v))
        
        # If the target is unreachable
        return -1
    
# Time Complexity: O((E + V) log V) where E is the number of edges and V is the number of vertices.
# Space Complexity: O(E + V) for the graph representation and the priority queue.