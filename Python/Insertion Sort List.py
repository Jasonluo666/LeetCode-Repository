# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ans = ListNode(0)
        scanner = head
        while scanner is not None:
            pointer = ans
            while pointer.next is not None and pointer.next.val < scanner.val:
                pointer = pointer.next
            
            temp = pointer.next
            pointer.next = scanner
            scanner = scanner.next
            pointer.next.next = temp
        
        return ans.next