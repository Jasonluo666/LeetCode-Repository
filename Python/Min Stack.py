class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        self.stack.append(x)
        if self.min is None or self.min > x:
            self.min = x
        

    def pop(self):
        """
        :rtype: None
        """
        
        val = self.stack.pop()
        if val == self.min:
            if len(self.stack) > 0:
                self.min = min(self.stack)
            else:
                self.min = None

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()