# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        self.index = len(postorder) - 1
        def construct(inorder, postorder):
            if not inorder or self.index < 0:
                return None
            
            if postorder[self.index] in inorder:
                index = inorder.index(postorder[self.index])
                root = TreeNode(postorder[self.index])
                self.index -= 1
                
                root.right = construct(inorder[index + 1:], postorder)
                root.left = construct(inorder[:index], postorder)
                return root
        
        return construct(inorder, postorder)