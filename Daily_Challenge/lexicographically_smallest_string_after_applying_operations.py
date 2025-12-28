#1625. Lexicographically Smallest String After Applying Operations

from collections import deque
from typing import List

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        
        # A queue for the BFS, starting with the initial string.
        q = deque([s])
        
        # A set to keep track of all reachable strings to avoid cycles.
        visited = {s}
        
        while q:
            current_s = q.popleft()
            
            # --- Operation 1: Add ---
            s_list = list(current_s)
            for i in range(1, n, 2):
                digit = int(s_list[i])
                s_list[i] = str((digit + a) % 10)
            s_add = "".join(s_list)
            
            if s_add not in visited:
                visited.add(s_add)
                q.append(s_add)

            # --- Operation 2: Rotate ---
            s_rot = current_s[-b:] + current_s[:-b]
            
            if s_rot not in visited:
                visited.add(s_rot)
                q.append(s_rot)
                
        # The answer is the lexicographically smallest string among all reachable states.
        return min(visited)
    
#Time Complexity: O(n * m) where n is the length of the string and m is the number of unique states reachable.
#Space Complexity: O(n * m) for storing all reachable states in the visited set.