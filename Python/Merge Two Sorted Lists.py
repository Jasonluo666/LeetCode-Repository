# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # create new list -> gradually construct the answer list
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val < l2.val:
            ans = l1
            p = l1.next
            q = l2
        else:
            ans = l2
            p = l2.next
            q = l1
            
        ans_point = ans
        while p is not None and q is not None:
            if p.val > q.val:
                ans_point.next = q
                ans_point = ans_point.next
                q = q.next
            else:
                ans_point.next = p
                ans_point = ans_point.next
                p = p.next
        
        if p is not None:
            ans_point.next = p
        else:
            ans_point.next = q
        
        return ans