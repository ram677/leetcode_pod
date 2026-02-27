#3666. Minimum Operations to Equalize Binary String

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        c = s.count('0')
        if c == 0:
            return 0
            
        n = len(s)
        low = c
        high = c
        parity = c % 2
        
        visited = set()
        visited.add((low, high, parity))
        
        ops = 0
        while True:
            ops += 1
            
            # 1. Calculate the new minimum possible '0's (new_low)
            # We want to minimize |i - k| for i in [low, high]
            if low <= k <= high:
                new_low = 0 if (low % 2 == k % 2) else 1
            elif k < low:
                new_low = low - k
            else:
                new_low = k - high
                
            # 2. Calculate the new maximum possible '0's (new_high)
            # We want to minimize |i - target_high| for i in [low, high] where target_high = n - k
            target_high = n - k
            if low <= target_high <= high:
                min_diff = 0 if (low % 2 == target_high % 2) else 1
            elif target_high < low:
                min_diff = low - target_high
            else:
                min_diff = target_high - high
                
            new_high = n - min_diff
            
            # Update interval and parity
            low = new_low
            high = new_high
            parity = (parity + k) % 2
            
            # If 0 is reachable, we are done
            if low == 0:
                return ops
                
            # Detect infinite loops (impossible to solve)
            state = (low, high, parity)
            if state in visited:
                return -1
                
            visited.add(state)

# Time Complexity: O(n) in the worst case, where n is the length of the string, due to the number of unique states we can encounter.
# Space Complexity: O(n) in the worst case, due to the visited set storing unique states.