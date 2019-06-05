# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(root1, root2):
            if root1 is None or root2 is None:
                if root1 is None and root2 is None:
                    return True
                else:
                    return False
            
            if root1.val != root2.val:
                return False
            
            pos1 = dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            pos2 = dfs(root1.right, root2.left) and dfs(root1.left, root2.right)
            return pos1 or pos2
        
        return dfs(root1, root2)