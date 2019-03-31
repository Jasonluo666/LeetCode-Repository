# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = ['']
        def dfs(root):
            if root is None:
                data[0] += 'x '
            else:
                data[0] += str(root.val) + ' '
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return data[0][:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        global index
        index = 0
        
        def dfs(data):
            global index
            if index > len(data) - 1 or data[index] == 'x':
                index += 2
                return None
            
            val = 0
            next_space = index
            while next_space < len(data) and data[next_space] != ' ':
                next_space += 1
            
            val = int(data[index:next_space])
            index = next_space + 1
            
            root = TreeNode(val)
            root.left = dfs(data)
            root.right = dfs(data)
            
            return root
        
        return dfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))