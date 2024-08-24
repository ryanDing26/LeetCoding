from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given the beginning of a linked list head, return true if there is a
        cycle in the linked list. Otherwise, return false.

        There is a cycle in a linked list if at least one node in the list that
        can be visited again by following the next pointer.
        Approach
        --------
        1. Create a fast and a slow pointer such that the fast pointer iterates
           over every two elements and the slow pointer iterates over every
           element.
        2. While the fast pointer has something to point to still, perform this
           iterative pattern detailed in Step 1.
        3. If the fast and slow pointer are at the same node, return True since
           that means a cycle has been detected.
        4. If the fast and slow pointers are never at the same node and the
           fast pointer reaches the end of the LinkedList, return False since
           that means there is no cycle in the LinkedList.

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False
