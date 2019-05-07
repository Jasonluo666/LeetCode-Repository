# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans_head = ListNode(0)
        
        def recursiveVisit(head):
            if head is None:
                return
            
            if head.next is not None:
                recursiveVisit(head.next).next = head
            else:
                ans_head.next = head
            
            head.next = None
            return head
        
        recursiveVisit(head)
        return ans_head.next