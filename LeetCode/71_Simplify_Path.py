# https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split('/')
        stack = []
        for each in dirs:
            if each == '.' or each == '':
                continue
            if each == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(each)
        return "/" + "/".join(stack)

s = Solution()
path = "/home//foo/"
print(s.simplifyPath(path))


