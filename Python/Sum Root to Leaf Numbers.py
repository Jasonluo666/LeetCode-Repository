# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        def recursive(root, val):
            if root is None:
                return
            
            val = val * 10 + root.val
            if root.left is None and root.right is None:
                self.ans += val
            
            recursive(root.left, val)
            recursive(root.right, val)
        
        recursive(root, 0)
        return self.ans