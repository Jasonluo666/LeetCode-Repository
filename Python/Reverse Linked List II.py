# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if n <= m:
            return head
        
        # recursive function -> reverse part of the linked list
        global start, end, reverse_head, pointer
        # record the head and tail of the reversed part
        start, end, reverse_head = ListNode(0), ListNode(0), ListNode(0)
        pointer = reverse_head
        
        def findReverse(current, index, m, n):
            global start, end, reverse_head, pointer
            
            if index < n + 1:
                findReverse(current.next, index + 1, m, n)
            
            if index == n + 1:
                end.next = current
            elif index == m - 1 or (m == 1 and index == n):
                start.next = current
            elif m <= index <= n:
                pointer.next = current
                pointer = pointer.next
                pointer.next = None
        
        findReverse(head, 1, m, n)
        start.next.next = reverse_head.next
        pointer.next = end.next
        
        if m == 1:
            return start.next
        else:
            return head