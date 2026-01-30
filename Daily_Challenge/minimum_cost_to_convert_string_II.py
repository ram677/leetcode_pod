#2977. Minimum Cost to Convert String II

from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Step 1: Map all unique strings involved in operations to integer IDs
        # We use a set to collect unique strings from both original and changed lists
        nodes = set(original) | set(changed)
        str_to_id = {s: i for i, s in enumerate(nodes)}
        num_nodes = len(nodes)
        
        # Optimization: We only need to check substring lengths that actually exist in our rules
        valid_lengths = set(len(s) for s in nodes)
        
        # Step 2: Initialize Graph and Edge Weights
        inf = float('inf')
        # dist[i][j] stores min cost to convert string with ID i to string with ID j
        dist = [[inf] * num_nodes for _ in range(num_nodes)]
        
        # Cost to convert a string to itself is 0
        for i in range(num_nodes):
            dist[i][i] = 0
            
        # Populate initial costs from input
        for o, c, w in zip(original, changed, cost):
            u = str_to_id[o]
            v = str_to_id[c]
            dist[u][v] = min(dist[u][v], w)
            
        # Step 3: Floyd-Warshall Algorithm for All-Pairs Shortest Path
        # This handles chained conversions like A -> B -> C
        for k in range(num_nodes):
            for i in range(num_nodes):
                if dist[i][k] == inf: continue
                for j in range(num_nodes):
                    if dist[k][j] == inf: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        # Step 4: Dynamic Programming on the source string
        n = len(source)
        # dp[i] = min cost to make source[i:] equal to target[i:]
        dp = [inf] * (n + 1)
        dp[n] = 0
        
        # Iterate backwards from the end of the string
        for i in range(n - 1, -1, -1):
            # Case 1: If characters match, we can potentially skip this index with 0 cost
            if source[i] == target[i]:
                dp[i] = dp[i+1]
            
            # Case 2: Try converting substrings starting at i with length L
            for length in valid_lengths:
                if i + length > n:
                    continue
                
                sub_s = source[i : i+length]
                sub_t = target[i : i+length]
                
                # Check if we have a valid transformation path in our graph
                # Both the start substring and target substring must be known nodes
                if sub_s in str_to_id and sub_t in str_to_id:
                    u = str_to_id[sub_s]
                    v = str_to_id[sub_t]
                    
                    if dist[u][v] < inf:
                        dp[i] = min(dp[i], dist[u][v] + dp[i+length])

        # If dp[0] is still infinity, it's impossible to convert source to target
        return dp[0] if dp[0] != inf else -1