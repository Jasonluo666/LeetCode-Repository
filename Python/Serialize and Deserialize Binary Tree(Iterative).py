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

        # Breadth First Search
        data = ''
        queue = [root]
        while len(queue) > 0:
            next_node = queue[0]
            queue = queue[1:]
            
            if next_node is None:
                data += 'x '
            else:
                data += str(next_node.val) + ' '
                queue.append(next_node.left)
                queue.append(next_node.right)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        index = 0
        root = None
        queue = []
        while index < len(data):
            if root is None:
                if data[index] == 'x':
                    return
                else:
                    num = ''
                    while data[index] != ' ':
                        num += data[index]
                        index += 1
                    index += 1

                    root = TreeNode(int(num))
                    queue.append(root)
            else:
                current_node = queue[0]
                queue = queue[1:]

                if data[index] == 'x':
                    current_node.left = None
                    index += 2
                else:
                    num = ''
                    while data[index] != ' ':
                        num += data[index]
                        index += 1
                    index += 1

                    current_node.left = TreeNode(int(num))
                    queue.append(current_node.left)

                if data[index] == 'x':
                    current_node.right = None
                    index += 2
                else:
                    num = ''
                    while data[index] != ' ':
                        num += data[index]
                        index += 1
                    index += 1

                    current_node.right = TreeNode(int(num))
                    queue.append(current_node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))