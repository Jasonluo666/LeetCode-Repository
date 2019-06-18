# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        before, after = ListNode(0), ListNode(0)
        before_tail, after_tail = before, after
        pointer = head
        while pointer is not None:
            if pointer.val < x:
                before_tail.next = pointer
                before_tail = before_tail.next
                pointer = pointer.next
                before_tail.next = None
            else:
                after_tail.next = pointer
                after_tail = after_tail.next
                pointer = pointer.next
                after_tail.next = None
        
        before_tail.next = after.next
        return before.next