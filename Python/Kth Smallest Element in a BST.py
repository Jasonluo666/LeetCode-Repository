# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        global counter
        counter = 0
        
        def dfs(node, k):
            global counter
            if node is None:
                return
            
            is_find = dfs(node.left, k)
            if is_find is not None:
                return is_find
            
            counter += 1
            if counter == k:
                return node.val
            
            is_find = dfs(node.right, k)
            if is_find is not None:
                return is_find
        
        return dfs(root, k)
        