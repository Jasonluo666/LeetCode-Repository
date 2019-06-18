# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if root is None:
                return
            
            left_node = dfs(root.left)
            right_node = dfs(root.right)
            if left_node is not None:
                left_node.right = root.right
                root.right = root.left
                root.left = None
            
            if right_node is not None:
                return right_node
            elif left_node is not None:
                return left_node
            return root
        
        dfs(root)