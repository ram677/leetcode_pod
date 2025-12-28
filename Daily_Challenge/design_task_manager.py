#3408. Design Task Manager

import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        """
        Initializes the task manager.
        - tasks_heap: A min-heap storing (-priority, -taskId) to find the max task.
        - task_info: A dictionary mapping taskId to (userId, priority) as the source of truth.
        """
        self.tasks_heap = []
        self.task_info = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        """Adds a new task to the system."""
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.tasks_heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        """Updates a task's priority, adding a new entry to the heap."""
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.tasks_heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        """Removes a task by invalidating it in the info map."""
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        """
        Finds and executes the valid top-priority task, cleaning up stale entries
        from the top of the heap along the way.
        """
        while self.tasks_heap:
            # Pop the potential top task from the heap
            neg_priority, neg_taskId = heapq.heappop(self.tasks_heap)
            taskId = -neg_taskId
            
            # Check if this task is valid:
            # 1. It must exist in our source of truth map.
            # 2. Its priority in the map must match what we popped from the heap.
            #    If it doesn't match, it's a stale entry from a past 'edit'.
            if taskId in self.task_info and self.task_info[taskId][1] == -neg_priority:
                # This is the valid top task.
                userId, _ = self.task_info[taskId]
                # Execute it by removing it from the system.
                del self.task_info[taskId]
                return userId
        
        # If the heap becomes empty, there are no tasks left.
        return -1
    
#Time Complexity:
# Initialization: O(n log n) for n tasks due to heap insertions.    
# add: O(log n) for heap insertion.
# edit: O(log n) for heap insertion.
# rmv: O(1) for dictionary deletion.
# execTop: O(log n) in the worst case if we have to pop multiple stale entries.
# - changeRating: O(log m) for pushing a new rating into the heap, where m is the number of foods in that cuisine.
# - highestRated: O(k log m) in the worst case, where k is the number of stale entries we might need to pop to find the valid top food.
# Space Complexity: O(n) for storing the tasks in the heap and dictionary.
#Where n is the number of tasks.