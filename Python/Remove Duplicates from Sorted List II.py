# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def recursive(head):
            if head is None:
                return head
            
            next = recursive(head.next)
            if head.next is not None and head.val == head.next.val:
                if next is not None:
                    if next == head.next:
                        return next.next
                    else:
                        return next
                else:
                    return None
            
            head.next = next
            return head
        
        return recursive(head)