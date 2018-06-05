# https://leetcode.com/problems/backspace-string-compare/description/
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def check_backspace(s):
            stack = []
            for each in s:
                if each == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(each)
            return stack

        return check_backspace(S) == check_backspace(T)
