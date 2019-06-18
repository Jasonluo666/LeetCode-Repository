# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        self.ans = []
        def dfs(root, val, sum, path):
            if root is None:
                return
            
            val += root.val
            path = path + [root.val]
            if root.left is None and root.right is None:
                if val == sum:
                    self.ans.append(path)
                return
            
            dfs(root.left, val, sum, path)
            dfs(root.right, val, sum, path)
        
        
        dfs(root, 0, sum, [])
        return self.ans