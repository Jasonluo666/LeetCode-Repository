# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        
        heads = []
        for index in range(len(lists)):
            if lists[index] is not None:
                heapq.heappush(heads, (lists[index].val, index, lists[index]))
        
        ans_head = ListNode(0)
        pointer = ans_head
        while len(heads) > 0:
            _, index, next_node = heapq.heappop(heads)
            
            temp = next_node
            next_node = next_node.next
            
            pointer.next = temp
            pointer = pointer.next
            
            if next_node is not None:
                heapq.heappush(heads, (next_node.val, index, next_node))
        
        return ans_head.next