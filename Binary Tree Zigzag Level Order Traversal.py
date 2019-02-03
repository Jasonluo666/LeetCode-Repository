# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # BFS
        # reverse the search queue everytime -> zigzag
        queue_1 = [root]
        queue_2 = []
        counter = 0
        ans = []
        
        while len(queue_1) > 0 or len(queue_2) > 0:
            ans.append([])
            if counter % 2 == 0:
                for node in queue_1:
                    if node is not None:
                        ans[-1].append(node.val)
                        queue_2.append(node.left)
                        queue_2.append(node.right)
                
                queue_2 = queue_2[::-1]
                queue_1 = []
            else:
                for node in queue_2:
                    if node is not None:
                        ans[-1].append(node.val)
                        queue_1.append(node.right)
                        queue_1.append(node.left)
                
                queue_1 = queue_1[::-1]
                queue_2 = []
            counter += 1
        
        if len(ans[-1]) == 0:
            ans.pop()
        
        return ans