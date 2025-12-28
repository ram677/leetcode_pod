#3217. Delete Nodes From Linked List Present in Array

from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Convert `nums` to a set for fast O(1) lookups.
        to_delete = set(nums)
        
        # 2. Create a dummy node. This simplifies edge cases
        #    like deleting the original head.
        dummy = ListNode(0, head)
        
        # 3. Use 'prev' and 'curr' pointers to traverse the list.
        #    'prev' points to the last node we kept.
        prev = dummy
        curr = head
        
        while curr:
            if curr.val in to_delete:
                # Delete 'curr' by bypassing it.
                # 'prev' does not move.
                prev.next = curr.next
            else:
                # 'curr' is a node we are keeping,
                # so 'prev' moves forward.
                prev = curr
            
            # 'curr' always moves to the next node.
            curr = curr.next
            
        # 4. The new head is the node after the dummy node.
        return dummy.next
    
# Time Complexity: O(m + n), where m is the length of the nums array
# and n is the number of nodes in the linked list.
# Space Complexity: O(m), for storing the set of values to delete.