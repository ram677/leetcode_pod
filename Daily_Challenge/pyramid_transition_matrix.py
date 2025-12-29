#756. Pyramid Transition Matrix

from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # 1. Preprocess 'allowed' into a lookup table
        # Key: (left, right), Value: list of valid top blocks
        transitions = defaultdict(list)
        for pattern in allowed:
            transitions[(pattern[0], pattern[1])].append(pattern[2])

        # Memoization cache to store results for specific rows
        memo = {}

        def can_build(row):
            # Base Case: If the row has only 1 block, we reached the top
            if len(row) == 1:
                return True
            
            # Check cache
            if row in memo:
                return memo[row]
            
            # We need to generate all possible 'next_row' strings
            # This requires a helper to build the row character by character
            
            results = []
            
            # Helper to build the next row via backtracking
            def build_next_row(index, current_next_row):
                # If we have built a full next row (length should be len(row) - 1)
                if index == len(row) - 1:
                    results.append("".join(current_next_row))
                    return
                
                # Get the base pair from the current row
                base_pair = (row[index], row[index+1])
                
                # If no pattern allows this base pair, this path is dead
                if base_pair not in transitions:
                    return
                
                # Try all allowed top blocks for this pair
                for top in transitions[base_pair]:
                    current_next_row.append(top)
                    build_next_row(index + 1, current_next_row)
                    current_next_row.pop() # Backtrack

            # Generate all valid next rows
            build_next_row(0, [])
            
            # Try to solve for any of the generated next rows
            for next_r in results:
                if can_build(next_r):
                    memo[row] = True
                    return True
            
            # If no path works
            memo[row] = False
            return False

        return can_build(bottom)
    
# Time Complexity: O(N * M^H) where N is the length of the bottom row, M is the number of allowed patterns, and H is the height of the pyramid.
# Space Complexity: O(M^H) for the memoization and recursion stack.