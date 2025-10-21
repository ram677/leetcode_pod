#3346. Maximum Frequency of an Element After Performing Operations I

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        from collections import Counter
        
        # Count original frequencies
        freq = Counter(nums)
        
        # Create events for sweep line
        # For each number, it can transform to any value in [num-k, num+k]
        events = []
        for num in nums:
            events.append((num - k, 1))      # Start of range
            events.append((num + k + 1, -1))  # End of range (exclusive)
        
        # Sort events by position
        events.sort()
        
        max_freq = 0
        current_reachable = 0
        i = 0
        
        # Get all unique values that could be targets
        all_values = set()
        for num in nums:
            all_values.add(num)
            all_values.add(num - k)
            all_values.add(num + k)
        
        sorted_values = sorted(all_values)
        
        # Process each potential target value
        event_idx = 0
        for target in sorted_values:
            # Process all events up to and including current target
            while event_idx < len(events) and events[event_idx][0] <= target:
                current_reachable += events[event_idx][1]
                event_idx += 1
            
            # Elements already at target
            already_there = freq[target]
            # Elements that can be transformed to target (excluding already there)
            can_transform = current_reachable - already_there
            
            # Maximum frequency for this target
            max_for_target = already_there + min(numOperations, can_transform)
            max_freq = max(max_freq, max_for_target)
        
        return max_freq
    
#Time Complexity: O(n log n) due to sorting events and unique values.
#Space Complexity: O(n) for storing events and frequency counts.
# where n is the number of elements in nums.
    
