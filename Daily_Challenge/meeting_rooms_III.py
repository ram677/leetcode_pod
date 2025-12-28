#2402. Meeting Rooms III

import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # 1. Sort meetings by start time to process them chronologically
        meetings.sort()
        
        # Min-heap for available room indices (initially all 0 to n-1)
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)
        
        # Min-heap for busy rooms: stores (end_time, room_index)
        busy_rooms = []
        
        # Track usage count for each room
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have finished by the time this meeting starts
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_idx)
            
            if available_rooms:
                # Scenario 1: A room is available. Pick the one with smallest index.
                room_idx = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room_idx))
            else:
                # Scenario 2: No room available. Wait for the earliest one to finish.
                # heap[0] gives the room with min end_time (and min index if ties)
                current_end, room_idx = heapq.heappop(busy_rooms)
                
                # The meeting is delayed. New duration = current_end + original_duration
                new_end = current_end + (end - start)
                heapq.heappush(busy_rooms, (new_end, room_idx))
                
            count[room_idx] += 1
            
        # Return index with max value. 
        # count.index(max_val) finds the *first* occurrence, handling the tie-break rule automatically.
        return count.index(max(count))
    
# Time Complexity: O(m log n), where m is the number of meetings and n is the number of rooms.
# Space Complexity: O(n), for the heaps and count array.