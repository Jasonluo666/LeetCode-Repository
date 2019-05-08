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
        
        self.data = ''
        
        def encode_inorder(root):
            if root is None:
                self.data += 'x '
                return
            
            self.data += str(root.val) + ' '
            encode_inorder(root.left)
            encode_inorder(root.right)
        
        encode_inorder(root)
        return self.data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        self.index = 0
        def decode_inorder(data):
            if data[self.index] == 'x':
                self.index += 2
                return
            
            num = ''
            while data[self.index] != ' ':
                num += data[self.index]
                self.index += 1
            self.index += 1
            
            root = TreeNode(int(num))
            root.left = decode_inorder(data)
            root.right = decode_inorder(data)
            
            return root
        
        return decode_inorder(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))