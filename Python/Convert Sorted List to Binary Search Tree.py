# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        pointers = []
        while head is not None:
            pointers.append(head.val)
            head = head.next
        
        def recursive(array):
            if not array:
                return None
            
            mid = int(len(array) / 2)
            root = TreeNode(array[mid])
            root.left = recursive(array[:mid])
            root.right = recursive(array[mid + 1:])
            return root
        
        return recursive(pointers)