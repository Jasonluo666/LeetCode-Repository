# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # find the previous node of the delete node, assign the pointer to skip the delete node
        ans_node = None
        current_node = head
        count = 0
        
        while current_node != None:
            if count == n:
                ans_node = head
            elif count > n:
                ans_node = ans_node.next
            
            count += 1
            current_node = current_node.next
        
        # delete the first node
        if ans_node is None:
            return head.next
        else:
            ans_node.next = ans_node.next.next
            return head