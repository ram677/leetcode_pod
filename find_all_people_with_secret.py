#2092. Find All People With Secret

from typing import List
from collections import defaultdict, deque
import itertools

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        # Set of people who know the secret
        known = {0, firstPerson}
        
        # Group meetings by time
        # itertools.groupby requires the list to be sorted by the key we are grouping by
        for time, group in itertools.groupby(meetings, key=lambda x: x[2]):
            current_meetings = list(group)
            
            # 1. Build the adjacency graph for this specific time slot
            graph = defaultdict(list)
            people_involved = set()
            
            for p1, p2, _ in current_meetings:
                graph[p1].append(p2)
                graph[p2].append(p1)
                people_involved.add(p1)
                people_involved.add(p2)
            
            # 2. Find all people in this batch who already know the secret
            # These will be the starting points for BFS
            queue = deque([p for p in people_involved if p in known])
            
            # Track visited within this time batch to avoid cycles/redundancy
            # Note: We can just use the 'known' set to prevent re-processing, 
            # but we need to ensure we add NEW people to 'known' as we find them.
            visited_in_batch = set(queue)
            
            # 3. BFS to propagate the secret instantaneously
            while queue:
                curr = queue.popleft()
                
                for neighbor in graph[curr]:
                    if neighbor not in known:
                        known.add(neighbor)
                        visited_in_batch.add(neighbor)
                        queue.append(neighbor)
                        
        return list(known)
    
# Time Complexity: O(M log M + M + N) where M is the number of meetings and N is the number of people.
# Space Complexity: O(N + M) for the graph and other data structures used.