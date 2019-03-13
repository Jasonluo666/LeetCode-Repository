# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return
        
        odd_head = None
        tail_pointer = None
        counter = 2
        
        pointer = head
        while pointer.next is not None:
            if odd_head is None:
                odd_head = pointer.next
                tail_pointer = pointer.next
            else:
                tail_pointer.next = pointer.next
                tail_pointer = tail_pointer.next
            
            pointer.next = pointer.next.next
            if pointer.next is not None:
                pointer = pointer.next
            
            tail_pointer.next = None
        
        pointer.next = odd_head
        return head