# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return None
            
            node = TreeNode(0)
            if root1 is not None:
                node.val += root1.val
            if root2 is not None:
                node.val += root2.val
            
            if root1 is None or root2 is None:
                if root1 is None:
                    node.left = dfs(None, root2.left)
                    node.right = dfs(None, root2.right)
                else:
                    node.left = dfs(root1.left, None)
                    node.right = dfs(root1.right, None)
            else:
                node.left = dfs(root1.left, root2.left)
                node.right = dfs(root1.right, root2.right)
            return node
        
        return dfs(t1, t2)