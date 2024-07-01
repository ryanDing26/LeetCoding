from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Level: Easy

        Problem Statement
        -----------------
        Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

        Approach
        --------
        Change the pointers.

        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        
        # Iterative, two pointers
        previous, current = None, head # before head, at head

        while curr:
            temp = current.next # need to save location of nonreversed LL ordering

            # Actual reversing process
            current.next = previous
            previous = current

            # Counter/condition checker
            current = temp

        return current # variable of new head

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead