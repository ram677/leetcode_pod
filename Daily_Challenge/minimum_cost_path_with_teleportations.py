#3651. Minimum Cost Path with Teleportations

import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # --- Preprocessing ---
        # Map each unique value to all coordinates containing that value
        # This allows us to efficiently "land" teleportations.
        val_to_coords = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val not in val_to_coords:
                    val_to_coords[val] = []
                val_to_coords[val].append((r, c))
        
        # Sort unique values to create the "Virtual Chain"
        sorted_vals = sorted(val_to_coords.keys())
        # Map actual values to their rank (index in sorted list)
        val_to_rank = {v: i for i, v in enumerate(sorted_vals)}
        num_unique = len(sorted_vals)
        
        # --- Dijkstra's Algorithm ---
        # Priority Queue stores: (cost, is_virtual, u, v, used_k)
        # is_virtual = 0: u, v are row, col
        # is_virtual = 1: u is rank, v is ignored
        pq = [(0, 0, 0, 0, 0)]
        
        # Distance arrays to track minimum cost to reach states
        # Physical: dist[used_k][row][col]
        dist_phys = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
        # Virtual: dist[used_k][val_rank]
        dist_virt = [[float('inf')] * num_unique for _ in range(k + 1)]
        
        # Initial state: At (0,0) with cost 0
        dist_phys[0][0][0] = 0
        
        while pq:
            cost, is_virtual, u, v, used_k = heapq.heappop(pq)
            
            # === CASE 1: Processing a Physical Node ===
            if is_virtual == 0:
                r, c = u, v
                
                # Pruning: If we found a cheaper way to this state already, skip
                if cost > dist_phys[used_k][r][c]:
                    continue
                
                # Goal Check
                if r == m - 1 and c == n - 1:
                    return cost
                
                # Action A: Normal Moves (Right, Down)
                # Cost increases by the value of the destination cell
                for dr, dc in [(0, 1), (1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        new_cost = cost + grid[nr][nc]
                        if new_cost < dist_phys[used_k][nr][nc]:
                            dist_phys[used_k][nr][nc] = new_cost
                            heapq.heappush(pq, (new_cost, 0, nr, nc, used_k))
                
                # Action B: Initiate Teleport
                # Move to the Virtual Node corresponding to current cell's value
                if used_k < k:
                    val = grid[r][c]
                    rank = val_to_rank[val]
                    # Cost to enter virtual network is 0
                    if cost < dist_virt[used_k][rank]:
                        dist_virt[used_k][rank] = cost
                        heapq.heappush(pq, (cost, 1, rank, -1, used_k))
            
            # === CASE 2: Processing a Virtual Node ===
            else:
                rank = u
                
                if cost > dist_virt[used_k][rank]:
                    continue
                
                # Action A: Propagate Down
                # If we can teleport from value V, we can also teleport from any value < V
                if rank > 0:
                    if cost < dist_virt[used_k][rank - 1]:
                        dist_virt[used_k][rank - 1] = cost
                        heapq.heappush(pq, (cost, 1, rank - 1, -1, used_k))
                
                # Action B: Land Teleport
                # Move from Virtual Node back to Physical Grid
                # This transition consumes 1 teleport (moves from used_k to used_k + 1)
                next_k = used_k + 1
                if next_k <= k:
                    val = sorted_vals[rank]
                    # Try landing on ALL cells with this specific value
                    for (Lr, Lc) in val_to_coords[val]:
                        if cost < dist_phys[next_k][Lr][Lc]:
                            dist_phys[next_k][Lr][Lc] = cost
                            heapq.heappush(pq, (cost, 0, Lr, Lc, next_k))
                            
        return -1
    
# Time Complexity: O((m * n + U) log(m * n + U)) where U is the number of unique values in the grid.
# Space Complexity: O(m * n + U) for distance arrays and value-to-coordinates mapping.