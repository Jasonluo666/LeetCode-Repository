# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # recursively visiting the tree
        # append the result to the ans list
        ans = []
        
        def visit_node(node, depth):
            if node is None:
                return
            
            if len(ans) == depth:
                ans.append([node.val])
            else:
                ans[depth].append(node.val)
            
            visit_node(node.left, depth + 1)
            visit_node(node.right, depth + 1)
        
        visit_node(root, 0)
        return ans