from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Level: Easy

        Problem Statement
        -----------------
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted linked list and return the head of
        the new sorted linked list.

        The new list should be made up of nodes from list1 and list2.


        Approach
        --------
        1. Create a new LinkedList, with a moving pointer to add elements and a
           dummy node to point to the head later on.
        2. While the heads of the two LinkedLists have content, meaning both
           list still have something to compare to one another:
             a. Compare the values stored at the head pointers. If the first
                head is less than the second head, make that the next element
                in the new LinkedList, and update the head pointer to point to
                the next element
             b. Update the moving pointer created in Step 1 to the next spot.
        3. If there are still some element that need to be put into the new
           LinkedList, that means there are greater than all the current
           elements already stored in the LinkedList and need to simply be
           appended to it.
        4. Return the next pointer of the dummy node that we had used to store
           the ListNode() head before; You need it to be the next pointer since
           the dummy node stored the element BEFORE the head, which was just a
           NoneType. 
          
        TC/SC
        -----
        TC: o(n), n being the longest LinkedList
        SC: O(n), n being the number of total elements in both LinkedLists

        '''
        # This stores some NoneType value before the head of the list, and will become the moving pointer to build the LinkedList on!
        new_head = ListNode()
        # This stores the head of this new LinkedList, to access later to return.
        dummy = new_head

        # While there are two head pointers in the LinkedList to compare
        while list1 and list2:
            if list1.val < list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next
            
        # Whatever is left over is already sorted and greater than what is already in the new LinkedList, just append it to the moving pointer!
        new_head.next = list1 or list2

        return dummy.next