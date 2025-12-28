#2528. Maximize the Minimum Powered City

from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        # 1. Calculate the initial power for each city using a sliding window.
        initial_power = [0] * n
        current_window_sum = sum(stations[0 : r + 1])
        initial_power[0] = current_window_sum
        
        for i in range(1, n):
            j_enter = i + r
            j_exit = i - 1 - r
            
            if j_enter < n:
                current_window_sum += stations[j_enter]
            if j_exit >= 0:
                current_window_sum -= stations[j_exit]
            initial_power[i] = current_window_sum

        # 2. The "check" function for our binary search.
        def is_possible(target_power: int) -> bool:
            k_remaining = k
            additions = [0] * n
            power_from_additions = 0
            
            for i in range(n):
                # Slide the window that sums power from *new* stations
                if i > 0:
                    j_exit = i - 1 - r
                    j_enter = i + r
                    if j_exit >= 0:
                        power_from_additions -= additions[j_exit]
                    if j_enter < n:
                        power_from_additions += additions[j_enter]
                
                current_total_power = initial_power[i] + power_from_additions
                
                if current_total_power < target_power:
                    needed = target_power - current_total_power
                    
                    if needed > k_remaining:
                        return False
                        
                    k_remaining -= needed
                    
                    # Place stations at the farthest reachable spot
                    j_placement = min(i + r, n - 1)
                    additions[j_placement] += needed
                    
                    # This new placement adds to our current power
                    power_from_additions += needed
            
            return True

        # 3. Binary Search for the answer
        low = 0
        high = sum(stations) + k + 1  # A safe upper bound
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
    
# Time Complexity: O(n log(max_power)), where max_power is the maximum possible power a city can have and n is the number of cities.
# Space Complexity: O(n) for the initial power and additions arrays.