# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        
        def dfs(root, current_sum):
            if root.right is not None:
                current_sum = dfs(root.right, current_sum)
            root.val += current_sum
            
            if root.left is not None:
                return dfs(root.left, root.val)
            else:
                return root.val
        dfs(root, 0)
        return root