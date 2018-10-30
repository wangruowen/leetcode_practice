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

    def backspaceCompare_v2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def helper(s):
            i, j = 0, 0
            s_list = list(s)
            while j < len(s_list):
                if s_list[j] != '#':
                    s_list[i] = s_list[j]
                    i += 1
                else:
                    i = max(i - 1, 0)
                j += 1
            return "".join(s_list[:i])

        return helper(S) == helper(T)

s = Solution()
S = "y#fo##f"
T = "y#f#o##f"
print(s.backspaceCompare_v2(S, T))