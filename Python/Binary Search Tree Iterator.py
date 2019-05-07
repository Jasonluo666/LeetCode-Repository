# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.cache = set()
        if not root:
            self.stack = []
        else:
            self.stack = [root]
            self.cache.add(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        ans = -1
        if len(self.stack) > 0:
            while self.stack[-1].left is not None and self.stack[-1].left not in self.cache:
                self.cache.add(self.stack[-1].left)
                self.stack.append(self.stack[-1].left)
            
            node = self.stack.pop()
            
            if node.right is not None and node.right not in self.cache:
                self.stack.append(node.right)
            
            ans = node.val
        return ans
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()