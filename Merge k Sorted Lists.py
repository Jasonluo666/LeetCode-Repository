# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # use the heap operation
        # everytime choose the smallest one from heap, replace it with the next element in that list
        import heapq
            
        if not lists:
            return None
                
        ans_heap = []
        for index in range(len(lists)):
            if lists[index] is not None:
                heapq.heappush(ans_heap,(lists[index].val, index))
        
        if len(ans_heap) == 0:
            return None
        
        ans = None
        ans_pointer = None
        while len(ans_heap) > 0:
            next_element = heapq.heappop(ans_heap)
            if ans is None:
                ans = lists[next_element[1]]
                ans_pointer = ans
            else:
                ans_pointer.next = lists[next_element[1]]
                ans_pointer = ans_pointer.next
            
            lists[next_element[1]] = lists[next_element[1]].next
            if lists[next_element[1]] is not None:
                heapq.heappush(ans_heap, (lists[next_element[1]].val, next_element[1]))
        
        return ans
        