#2211. Count Collisions on a Road

class Solution:
    def countCollisions(self, directions: str) -> int:
        # 1. Remove cars moving 'L' from the start (they drive away safely).
        #    Example: "LLRL..." -> "RL..."
        temp = directions.lstrip('L')
        
        # 2. Remove cars moving 'R' from the end (they drive away safely).
        #    Example: "...RLRR" -> "...RL"
        temp = temp.rstrip('R')
        
        # 3. In the remaining substring, every moving car ('L' or 'R') 
        #    is sandwiched between obstacles and will eventually collide.
        #    Stationary cars ('S') do not add to the collision count themselves,
        #    but they act as walls for others.
        #    So, we just count everything that is NOT 'S'.
        return len(temp) - temp.count('S')
    
#Time Complexity: O(n), where n is the length of the input string.
#Space Complexity: O(1), since we are using a constant amount of extra space.