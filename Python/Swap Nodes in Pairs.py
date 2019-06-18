# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def recursive(head):
            if head is None or head.next is None:
                return head
            
            temp = head
            head = head.next
            temp.next = head.next
            head.next = temp

            temp.next = recursive(temp.next)
            return head
        
        return recursive(head)