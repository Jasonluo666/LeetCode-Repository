# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        # flatten the list in the first place and then pop elements like stack
        self.flatten_list = []
        self.flatten(nestedList)
        self.flatten_list = self.flatten_list[::-1]
    
    def flatten(self, nestedList):
        for element in nestedList:
            if element.isInteger():
                self.flatten_list.append(element.getInteger())
            else:
                self.flatten(element.getList())
        
    def next(self):
        """
        :rtype: int
        """
        return self.flatten_list.pop()
                

    def hasNext(self):
        """
        :rtype: bool
        """
        # check if the stack is empty
        return len(self.flatten_list) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())