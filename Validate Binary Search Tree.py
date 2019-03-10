# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        # search through the binary search tree -> node should meet the upper/lower bounds
        def dfs(root, min_val, max_val):
            if root is None:
                return True
            
            if (min_val is None or root.val > min_val) and (max_val is None or root.val < max_val):
                return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
            else:
                return False
            
        
        return dfs(root, None, None)