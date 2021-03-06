# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ans = None
        point = None
        point1 = l1
        point2 = l2
        carry = 0
        simple_sum = 0
        
        # simple calculator -> simulation of an adder

        while (point1 is not None) and (point2 is not None):
            simple_sum = point1.val + point2.val + carry
            if simple_sum >= 10:
                carry = 1
                simple_sum %= 10
            else:
                carry = 0
            
            if ans is None:
                ans = ListNode(simple_sum)
                point = ans
            else:
                point.next = ListNode(simple_sum)
                point = point.next
            
            point1 = point1.next
            point2 = point2.next
        
        while point1 is not None:
            point.next = ListNode(point1.val)
            point = point.next
            point1 = point1.next
            
            point.val += carry
            if point.val >= 10:
                carry = 1
                point.val %= 10
            else:
                carry = 0
        
        while point2 is not None:
            point.next = ListNode(point2.val)
            point = point.next
            point2 = point2.next
            
            point.val += carry
            if point.val >= 10:
                carry = 1
                point.val %= 10
            else:
                carry = 0
        
        if carry == 1:
            point.next = ListNode(carry)
        
        return ans

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        self.carry = 0
        def recursive(l1, l2):
            if l1 is None and l2 is None:
                if self.carry == 0:
                    return None
                else:
                    return ListNode(1)
            
            if l1 is None or l2 is None:
                if l1 is None:
                    node = ListNode(l2.val + self.carry)
                    self.carry = int(node.val / 10)
                    node.val %= 10
                    node.next = recursive(l1, l2.next)
                else:
                    node = ListNode(l1.val + self.carry)
                    self.carry = int(node.val / 10)
                    node.val %= 10
                    node.next = recursive(l1.next, l2)
            else:
                node = ListNode(l1.val + l2.val + self.carry)
                self.carry = int(node.val / 10)
                node.val %= 10
                node.next = recursive(l1.next, l2.next)
            return node
        
        return recursive(l1, l2)