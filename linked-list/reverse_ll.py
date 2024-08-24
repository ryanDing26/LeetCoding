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
        Given the beginning of a singly linked list head, reverse the list, and
        return the new beginning of the list.

        Approach
        --------
        1. Get the pointer of the element before the head (just a NoneType) and
           the head itself.
        2. While the 'head' is not a NoneType, meaning just before it hits the
           end of the original LinkedList:
             a. Store the element that is ACTUALLY after the head in a
                temporary variable to go to later, so that we can iterate over
                the LinkedList without issue.
             b. Set the next pointer of the current node to the previous node.
             c. Move the previous node forward to be the current node, and the
                current node to be the one ACTUALLY after the head in the
                non-reversed list (that we stored prior).
        3. Return the current node being pointed to, which is the new head of
           the reversed LinkedList.
           
        TC/SC
        -----
        TC: O(n)
        SC: O(1)
        '''
        
        # Iterative, two pointers
        previous, current = None, head # before head, at head

        while current:
            # This is where we go after we reverse previous and current; this is used to store current assignments before modifying them 
            temp = current.next

            # Actual reversing process
            # 1. The next element is actually the one before it
            # 2. The previous element can move forward by one spot
            current.next = previous 
            

            # These lines of code enable you to go to the next element to repeat the process
            previous = current
            current = temp

        return current # variable of new head
    
        # Recursive approach
        # if not head:
        #     return None

        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        # return newHead