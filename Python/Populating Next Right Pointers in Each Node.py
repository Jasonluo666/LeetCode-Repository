"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        def dfs(root):
            if root is None:
                return
            
            if root.left is not None:
                root.left.next = root.right
                if root.next is not None:
                    root.right.next = root.next.left
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return root