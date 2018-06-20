# https://leetcode.com/problems/flatten-nested-list-iterator/description/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
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

from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # stack
        self.stack = deque(nestedList)

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.popleft()
        return top.getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) > 0:
            top = self.stack[0]
            while not top.isInteger():
                top = self.stack.popleft()
                for each in reversed(top.getList()):
                    self.stack.appendleft(each)
                if len(self.stack) == 0:
                    break
                top = self.stack[0]
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())