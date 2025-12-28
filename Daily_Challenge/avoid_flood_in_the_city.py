#1488. Avoid Flood in The City

import collections
import heapq
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        
        # 1. Pre-computation: Find the next rainy day for each lake
        next_rain_map = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            if lake > 0:
                next_rain_map[lake].append(i)

        full_lakes = set()
        # Min-heap stores (next_rain_day, lake_number) for full lakes
        lakes_to_dry = [] 

        for i, lake in enumerate(rains):
            if lake > 0:
                # On a rainy day, remove the current day from the schedule
                next_rain_map[lake].popleft()

                if lake in full_lakes:
                    # It rained on an already full lake -> flood
                    return []
                
                full_lakes.add(lake)
                
                # If this lake will rain again, add it to the heap of tasks
                if next_rain_map[lake]:
                    next_day = next_rain_map[lake][0]
                    heapq.heappush(lakes_to_dry, (next_day, lake))
            else: # This is a dry day
                if lakes_to_dry:
                    # There's a pending flood, so we must act.
                    # Pop the lake that will rain again the soonest.
                    _, lake_to_dry = heapq.heappop(lakes_to_dry)
                    ans[i] = lake_to_dry
                    full_lakes.remove(lake_to_dry)
                else:
                    # No urgent tasks, we can dry any lake (e.g., lake 1)
                    ans[i] = 1
        
        return ans
    
# Time Complexity: O(n log k) where n is the number of days and k is the number of unique lakes.
# Space Complexity: O(n) for the next_rain_map and the heap in the worst case.