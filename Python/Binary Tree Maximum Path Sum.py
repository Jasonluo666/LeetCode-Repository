# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global ans
        ans = root.val

        # depth first search the tree -> calculate each local maximum and update the global max
        def dfs(root):
            global ans
            if root is None:
                return 0
            
            left_val, right_val = max(0, dfs(root.left)), max(0, dfs(root.right))
            ans = max(ans, root.val + left_val + right_val)
            
            return max(root.val + left_val, root.val + right_val)
        
        dfs(root)
        return ans