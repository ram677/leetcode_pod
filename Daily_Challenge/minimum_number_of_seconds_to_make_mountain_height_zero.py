#3296. Minimum Number of Seconds to Make Mountain Height Zero

import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        low = 1
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        def can_reduce(time_limit: int) -> bool:
            reduced = 0
            for w in workerTimes:
                max_x = (math.isqrt(8 * time_limit // w + 1) - 1) // 2
                reduced += max_x
                if reduced >= mountainHeight:
                    return True
            return False
            
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_reduce(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
    
# Time Complexity: O(n log(mountainHeight^2 * min(workerTimes))), where n is the number of workers. The binary search runs in O(log(mountainHeight^2 * min(workerTimes))) time, and the can_reduce function runs in O(n) time for each iteration of the binary search.
# Space Complexity: O(1), as we are using only a constant amount of extra space.