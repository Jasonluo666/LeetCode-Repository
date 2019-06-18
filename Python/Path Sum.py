# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def dfs(root, val, sum):
            if root is None:
                return False
            
            val += root.val
            if root.left is None and root.right is None:
                return val == sum
            
            return dfs(root.left, val, sum) or dfs(root.right, val, sum)
        
        return dfs(root, 0, sum)