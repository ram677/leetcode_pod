#2872. Maximum Number of K-Divisible Components

import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(100000)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        # 1. Build the graph (Adjacency List)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.components_count = 0
        
        # 2. Define DFS function
        def dfs(current_node, parent):
            # Start with the value of the current node
            current_sum = values[current_node]
            
            # Add sums from all children
            for neighbor in adj[current_node]:
                if neighbor != parent:
                    current_sum += dfs(neighbor, current_node)
            
            # 3. Check if the current subtree sum is divisible by k
            if current_sum % k == 0:
                self.components_count += 1
                # If we cut this component off, it contributes 0 to the parent
                return 0
            
            # Otherwise, return the sum to be added to the parent
            return current_sum

        # 4. Start DFS from node 0
        dfs(0, -1)
        
        return self.components_count
    
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(n) for the adjacency list and recursion stack.