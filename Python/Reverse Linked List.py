# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None
        
        # pointer always contains the current first element
        pointer = head
        while head.next is not None:
            pointer_next = head.next
            
            head.next = pointer_next.next
            pointer_next.next = pointer
            # update the pointer
            pointer = pointer_next
        
        return pointer