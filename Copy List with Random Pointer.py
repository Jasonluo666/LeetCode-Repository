"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return
        
        # mapping the orignal position to the copied one
        copied_head = Node(head.val, head.next, head.random)
        addr_map = {head: copied_head}
        
        pointer_origin = head.next
        pointer_copied = copied_head
        while pointer_origin is not None:
            pointer_copied.next = Node(pointer_origin.val, pointer_origin.next, pointer_origin.random)
            pointer_copied = pointer_copied.next
            
            addr_map[pointer_origin] = pointer_copied
            
            pointer_origin = pointer_origin.next
        
        pointer_copied = copied_head
        while pointer_copied is not None:
            if pointer_copied.random is not None:
                pointer_copied.random = addr_map[pointer_copied.random]
            pointer_copied = pointer_copied.next
        
        return copied_head
        
        
        
        
        return copied_head