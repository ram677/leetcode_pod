#3459. Length of Longest V-Shaped Diagonal Segment

from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # dp1[dir]: segments starting with 1. dir -> 0:from_tl, 1:from_tr, 2:from_bl, 3:from_br
        dp1 = [[[0] * 4 for _ in range(m)] for _ in range(n)]
        
        # dpc[dir]: continuation segments. dir -> 0:to_br, 1:to_bl, 2:to_tl, 3:to_tr
        # Each entry stores (len_starts_with_0, len_starts_with_2)
        dpc = [[[(0, 0)] * 4 for _ in range(m)] for _ in range(n)]

        # --- Calculate dp1 tables (segments starting with 1) ---
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1: dp1[r][c][0], dp1[r][c][1] = 1, 1
                else:
                    if r > 0 and c > 0 and dp1[r-1][c-1][0] > 0 and grid[r][c] == (2 if dp1[r-1][c-1][0] % 2 != 0 else 0):
                        dp1[r][c][0] = dp1[r-1][c-1][0] + 1
                    if r > 0 and c < m - 1 and dp1[r-1][c+1][1] > 0 and grid[r][c] == (2 if dp1[r-1][c+1][1] % 2 != 0 else 0):
                        dp1[r][c][1] = dp1[r-1][c+1][1] + 1
        
        for r in range(n - 1, -1, -1):
            for c in range(m):
                if grid[r][c] == 1: dp1[r][c][2], dp1[r][c][3] = 1, 1
                else:
                    if r < n - 1 and c > 0 and dp1[r+1][c-1][2] > 0 and grid[r][c] == (2 if dp1[r+1][c-1][2] % 2 != 0 else 0):
                        dp1[r][c][2] = dp1[r+1][c-1][2] + 1
                    if r < n - 1 and c < m - 1 and dp1[r+1][c+1][3] > 0 and grid[r][c] == (2 if dp1[r+1][c+1][3] % 2 != 0 else 0):
                        dp1[r][c][3] = dp1[r+1][c+1][3] + 1

        # --- Calculate dpc tables (continuation segments) ---
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                # to_br
                l0, l2 = 0, 0
                if grid[r][c] == 0: l0 = 1 + (dpc[r+1][c+1][0][1] if r < n-1 and c < m-1 else 0)
                if grid[r][c] == 2: l2 = 1 + (dpc[r+1][c+1][0][0] if r < n-1 and c < m-1 else 0)
                dpc[r][c][0] = (l0, l2)
                # to_bl
                l0, l2 = 0, 0
                if grid[r][c] == 0: l0 = 1 + (dpc[r+1][c-1][1][1] if r < n-1 and c > 0 else 0)
                if grid[r][c] == 2: l2 = 1 + (dpc[r+1][c-1][1][0] if r < n-1 and c > 0 else 0)
                dpc[r][c][1] = (l0, l2)

        for r in range(n):
            for c in range(m):
                # to_tl
                l0, l2 = 0, 0
                if grid[r][c] == 0: l0 = 1 + (dpc[r-1][c-1][2][1] if r > 0 and c > 0 else 0)
                if grid[r][c] == 2: l2 = 1 + (dpc[r-1][c-1][2][0] if r > 0 and c > 0 else 0)
                dpc[r][c][2] = (l0, l2)
                # to_tr
                l0, l2 = 0, 0
                if grid[r][c] == 0: l0 = 1 + (dpc[r-1][c+1][3][1] if r > 0 and c < m-1 else 0)
                if grid[r][c] == 2: l2 = 1 + (dpc[r-1][c+1][3][0] if r > 0 and c < m-1 else 0)
                dpc[r][c][3] = (l0, l2)

        # --- Combine and find max_len ---
        max_len = 0
        turn_map = {0: 1, 1: 2, 2: 0, 3: 3} # Maps incoming leg dir to outgoing continuation dir
        turn_deltas = {0: (1,-1), 1: (-1,-1), 2: (1,1), 3: (-1,1)}

        for r in range(n):
            for c in range(m):
                max_len = max(max_len, dp1[r][c][0], dp1[r][c][1], dp1[r][c][2], dp1[r][c][3])
                for in_dir in range(4):
                    L1 = dp1[r][c][in_dir]
                    if L1 > 0:
                        out_dir_idx = turn_map[in_dir]
                        dr, dc = turn_deltas[in_dir]
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m:
                            expected = 0 if L1 % 2 == 0 else 2
                            l0, l2 = dpc[nr][nc][out_dir_idx]
                            L2 = l0 if expected == 0 else l2
                            max_len = max(max_len, L1 + L2)
        return max_len
    
#Time Complexity: O(n*m), where n and m are the dimensions of the grid
#Space Complexity: O(n*m), for the dp1 and dpc tables