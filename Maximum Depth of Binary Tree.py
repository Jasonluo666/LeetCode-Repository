# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root, depth):
            if root is None:
                return depth - 1
            else:
                return max(dfs(root.left, depth+1), dfs(root.right,depth+1))
        
        if root is None:
            return 0
        else:
            return dfs(root, 1)
        
        