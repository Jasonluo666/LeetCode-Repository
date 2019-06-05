# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        
        def recursive(root):
            if root is None:
                return 0
            
            left, right = recursive(root.left), recursive(root.right)
            self.ans = max(self.ans, left + right)
            
            return 1 + max(left, right)
        
        recursive(root)
        return self.ans