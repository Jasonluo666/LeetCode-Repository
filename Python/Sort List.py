# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        
        # O(nlongn), sort in-place
        def mergesort(head, length):
            if length == 1:
                return head
            
            half_len = int(length / 2)
            left_head = head
            
            # find head of the right list, set the tail of the left one to None
            right_head = head
            pos = 0
            while pos < half_len - 1:
                right_head = right_head.next
                pos += 1
            
            temp = right_head
            right_head = right_head.next
            temp.next = None
            left, right = mergesort(left_head, half_len), mergesort(right_head, length - half_len)
            
            # merge two sorted lists
            merged = None
            while left is not None and right is not None:
                current_min = None
                if left.val < right.val:
                    current_min = left
                    left = left.next
                else:
                    current_min = right
                    right = right.next
                
                if merged is None:
                    merged = current_min
                    head = current_min
                else:
                    merged.next = current_min
                    merged = merged.next
            
            # append unadded elements to the tail
            if left is not None:
                merged.next = left
            else:
                merged.next = right
            return head
    
        length = 0
        pointer = head
        while pointer is not None:
            length += 1
            pointer = pointer.next

        return mergesort(head, length)