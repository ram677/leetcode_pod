#3433. Count Mentions Per User

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # We need to process events in chronological order.
        # If timestamps are equal, OFFLINE events must be processed before MESSAGE events.
        # We create a list of tuples: (timestamp, type_rank, event_data)
        # type_rank: 0 for OFFLINE, 1 for MESSAGE
        sorted_events = []
        for event in events:
            timestamp = int(event[1])
            type_rank = 0 if event[0] == "OFFLINE" else 1
            sorted_events.append((timestamp, type_rank, event))
            
        # Sort by timestamp, then by type_rank
        sorted_events.sort(key=lambda x: (x[0], x[1]))
        
        # Array to store the result
        mentions = [0] * numberOfUsers
        
        # Array to store the time when a user comes back online.
        # Initialized to 0 because everyone is online at the start.
        online_time = [0] * numberOfUsers
        
        for ts, _, data in sorted_events:
            event_type = data[0]
            
            if event_type == "OFFLINE":
                user_id = int(data[2])
                # User becomes offline at 'ts' and comes back online at 'ts + 60'
                online_time[user_id] = ts + 60
                
            else: # MESSAGE
                mention_string = data[2]
                
                if mention_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                        
                elif mention_string == "HERE":
                    for i in range(numberOfUsers):
                        # User is online if their scheduled return time is <= current time
                        if online_time[i] <= ts:
                            mentions[i] += 1
                            
                else:
                    # Specific IDs like "id0 id1 id0"
                    ids = mention_string.split(" ")
                    for token in ids:
                        # Extract the number from "id<number>"
                        uid = int(token[2:])
                        mentions[uid] += 1
                        
        return mentions
    
# Time Complexity: O(m log m + n), where m is the number of events and n is the number of users.
# Space Complexity: O(m + n), for storing the sorted events and mentions.