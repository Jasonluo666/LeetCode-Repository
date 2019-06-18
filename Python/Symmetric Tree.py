# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = [(1, root.left, True), (1, root.right, False)]
        
        depth, node, is_left = queue[0]
        queue = queue[1:]
        
        while len(queue) > 0:
            left = []
            right = []
            
            current_depth = depth
            while depth == current_depth:
                if node is not None:
                    if is_left:
                        left.append(node.val)
                    else:
                        right.append(node.val)

                    queue.append((depth + 1, node.left, is_left))
                    queue.append((depth + 1, node.right, is_left))
                else:
                    if is_left:
                        left.append(None)
                    else:
                        right.append(None)
                
                if not queue:
                    break
                depth, node, is_left = queue[0]
                queue = queue[1:]
            
            if left != right[::-1]:
                return False
        return True