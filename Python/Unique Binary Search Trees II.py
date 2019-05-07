# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        
        # depth first search for possible sub_roots
        def dfs(min_val, max_val):
            if min_val > max_val:
                return [None]
            
            roots = []
            for element in range(min_val, max_val + 1):
                
                lefts = dfs(min_val, element - 1)
                rights = dfs(element + 1, max_val)
                for left in lefts:
                    for right in rights:
                        current_root = TreeNode(element)
                        current_root.left = left
                        current_root.right = right
                        roots.append(current_root)

            return roots
        
        return dfs(1, n)