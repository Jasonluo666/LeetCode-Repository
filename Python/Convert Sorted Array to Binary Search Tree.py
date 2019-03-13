# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # recursive function, construct the binary search tree like mergesort
        def create_subtree(array):
            if len(array) > 0:
                mid_index = int(len(array) / 2)
                root = TreeNode(array[mid_index])

                root.left = create_subtree(array[:mid_index])
                root.right = create_subtree(array[mid_index + 1:])

                return root
            else:
                return
        
        return create_subtree(nums)