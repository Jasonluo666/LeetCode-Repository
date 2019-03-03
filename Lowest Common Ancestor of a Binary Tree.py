# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p is None or q is None:
            return
        
        # depth first search
        def dfs(root):
            if root is None or self.ans is not None:
                return False
            
            # ancestor node with p or q
            if root.val == p.val or root.val == q.val:
                if dfs(root.left) == True or dfs(root.right) == True:
                    self.ans = root
                return True
            
            # ancestor node without p or q
            left, right = dfs(root.left), dfs(root.right)
            if left or right:
                if left and right:
                    self.ans = root
                return True
            
            return False
        
        dfs(root)
        return self.ans