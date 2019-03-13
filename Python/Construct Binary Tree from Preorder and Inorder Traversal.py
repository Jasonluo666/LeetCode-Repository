# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # use preorder as index -> root node
        # divide and conquer inorder
        current_index = [0]
        def dfs(inorder_array):
            if len(inorder_array) == 0:
                return
            
            # find the root in current inorder
            root_pos =None
            for index in range(len(inorder_array)):
                if inorder_array[index] == preorder[current_index[0]]:
                    root_pos = index
                    break
            
            # the root node belongs to this branch -> append the new root node
            if root_pos is not None:
                current_index[0] += 1
                sub_root = TreeNode(inorder_array[root_pos])
                left = inorder_array[:root_pos]
                right = inorder_array[root_pos + 1:]
                sub_root.left = dfs(left)
                sub_root.right = dfs(right)

                return sub_root
            else:
                return
        
        return dfs(inorder)