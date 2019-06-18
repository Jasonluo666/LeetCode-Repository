# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverseK(head, k):
            if k == 1:
                return head, head, head.next
            if head.next is None:
                return None, None, None
            
            front_node, top, next = reverseK(head.next, k - 1)
            if front_node is not None:
                front_node.next = head
                head.next = None

                return head, top, next
            else:
                return None, None, None
        
        def globalReverse(head):
            if head is None:
                return
            
            tail, this_head, next = reverseK(head, k)
            if tail is not None:
                tail.next = globalReverse(next)
                return this_head
            else:
                return head
        
        return globalReverse(head)