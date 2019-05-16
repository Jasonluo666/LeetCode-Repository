# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.ans = 0
        
        # dfs -> update local maximal ans
        def findLength(root, value):
            if root is None:
                return 0
            
            left = findLength(root.left, root.val)
            right = findLength(root.right, root.val)
            self.ans = max(self.ans, left + right)
            
            # return for the root func's calculations
            if root.val != value:
                return 0    
            else:
                return max(left, right) + 1
        
        findLength(root, root.val)
        
        return self.ans