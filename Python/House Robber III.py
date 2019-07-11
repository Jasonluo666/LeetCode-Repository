# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            if root is None:
                return 0, 0
            
            left_rob, left_leave = dfs(root.left)
            right_rob, right_leave = dfs(root.right)
            
            rob = left_leave + right_leave + root.val
            leave = max(left_rob, left_leave) + max(right_rob, right_leave)
            return rob, leave
        
        rob, leave = dfs(root)
        return max(rob, leave)