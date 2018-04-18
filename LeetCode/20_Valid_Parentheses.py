# https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {"{":"}", "[":"]", "(":")"}
        stack = []
        for each in s:
            if each in map:
                stack.append(each)
            else:
                if len(stack) > 0 and stack[-1] in map and map[stack[-1]] == each:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

s = Solution()
print(s.isValid("([)"))