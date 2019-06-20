# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.ans = []
#         def dfs(root):
#             if root is None:
#                 return
            
#             self.ans.append(root.val)
#             dfs(root.left)
#             dfs(root.right)
#         dfs(root)


        stack = [root]
        while len(stack) > 0:
            root = stack.pop()
            
            if root is not None:
                self.ans.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
            
        return self.ans