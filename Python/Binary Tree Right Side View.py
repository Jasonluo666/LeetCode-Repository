# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.ans = []
        def dfs(root, depth):
            if root is None:
                return
            
            if depth == len(self.ans):
                self.ans.append(root.val)
            
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        dfs(root, 0)
        return self.ans