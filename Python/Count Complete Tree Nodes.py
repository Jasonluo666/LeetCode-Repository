# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        self.max_depth = None
        self.count = 0
        self.is_finish = False
        def dfs(root, depth=0):
            if self.is_finish:
                return
            
            if root is None:
                if self.max_depth is None or self.max_depth == depth - 1:
                    self.max_depth = depth - 1
                    self.count += 1
                    return
                else:
                    self.is_finish = True
                    return
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root)
        
        return 2 ** self.max_depth + (self.count / 2) - 1