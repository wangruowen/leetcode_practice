# https://leetcode.com/problems/mini-parser/description/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    pass

#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        cur_nest_int, cur_num, sign = None, None, 1
        for c in s:
            if c == '-':
                sign = -1
            elif c.isdigit():
                if cur_num is None:
                    cur_num = 0
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                # new list
                new_int = NestedInteger()
                if cur_nest_int:
                    cur_nest_int.add(new_int)
                    stack.append(cur_nest_int)
                cur_nest_int = new_int
            elif c == ']':
                # Previous nested list finished, back to one up level
                if cur_num is not None:
                    cur_nest_int.add(cur_num * sign)
                    cur_num, sign = None, 1
                if len(stack) > 0:
                    cur_nest_int = stack.pop()
            elif c == ',':
                if cur_num is not None:
                    cur_nest_int.add(cur_num * sign)
                    cur_num, sign = None, 1

        if not cur_nest_int:
            # No list is encountered
            cur_nest_int = NestedInteger(cur_num * sign)

        return cur_nest_int

