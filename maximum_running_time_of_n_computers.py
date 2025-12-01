#2141. Maximum Running Time of N Computers

class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        # Lower bound: 1 (or min(batteries) technically)
        # Upper bound: Theoretical max is total energy divided by n computers
        left, right = 1, sum(batteries) // n
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if it's possible to run n computers for 'mid' minutes
            # Total energy required for n computers for 'mid' minutes is n * mid
            
            # Calculate total usable energy from all batteries for duration 'mid'.
            # A battery can contribute at most 'mid' minutes.
            # If battery > mid, it contributes 'mid'.
            # If battery < mid, it contributes its full charge.
            total_power = 0
            for battery in batteries:
                if battery < mid:
                    total_power += battery
                else:
                    total_power += mid
            
            if total_power >= n * mid:
                # If possible, try to run longer
                left = mid + 1
            else:
                # If not possible, reduce the time
                right = mid - 1
                
        return right
    
# Time Complexity: O(m), where m is the number of batteries.
# Space Complexity: O(1), no extra space used apart from variables.