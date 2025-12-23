#2054. Two Best Non-Overlapping Events

import heapq

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort()
        
        # Min-heap to store (end_time, value) of processed events
        # We use a min-heap to efficiently find events that end before the current event starts
        min_heap = []
        
        max_value_sum = 0
        max_seen_value = 0
        
        for start, end, value in events:
            # Pop all events from the heap that end before the current event starts.
            # Since the current event starts at 'start', a compatible previous event 
            # must end at 'start - 1' or earlier.
            while min_heap and min_heap[0][0] < start:
                # Update the max value of any single event that has finished
                max_seen_value = max(max_seen_value, heapq.heappop(min_heap)[1])
            
            # Option 1: Combine current event with the best non-overlapping previous event
            # Option 2: Just the current event (implicitly covered if max_seen_value is 0)
            # Option 3: Previous best result
            max_value_sum = max(max_value_sum, max_seen_value + value)
            
            # Add the current event to the heap for future consideration
            heapq.heappush(min_heap, (end, value))
            
        return max_value_sum

# Time Complexity: O(N log N) due to sorting and heap operations, where N is the number of events.
# Space Complexity: O(N) for the heap in the worst case.