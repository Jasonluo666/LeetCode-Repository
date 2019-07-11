# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        ans = []
        while head is not None:
            ans.append(head.val)
            head = head.next
        
        index = 0
        while index < len(ans) / 2:
            if ans[index] == ans[-index - 1]:
                index += 1
            else:
                break
        
        return index >= len(ans) / 2