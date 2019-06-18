# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        length = 0
        pointer = head
        tail = None
        while pointer is not None:
            if pointer.next is None:
                tail = pointer
            pointer = pointer.next
            length += 1
        
        if length == 0 or length == 1 or k % length == 0:
            return head
        
        remain = length - k % length
        
        ans = head
        while remain > 1:
            ans = ans.next
            remain -= 1
        
        temp = ans
        ans = ans.next
        temp.next = None
        
        tail.next = head
        return ans