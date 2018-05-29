# https://leetcode.com/problems/generate-parentheses/description/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Note that
        # new_set = set(["(%s)" % exist_parentheses,
        #                "()%s" % exist_parentheses,
        #                "%s()" % exist_parentheses])
        # this doesn't work
        total_set = []
        self.helper(n, total_set, set([""]))
        return total_set

    def helper(self, n, total_set, exist_set):
        if n == 0:
            total_set.extend(list(exist_set))
        else:
            new_set = set()
            for each in exist_set:
                for i in range(len(each) + 1):
                    # insert () to every gap of previous parentheses, including before and after previous parentheses
                    new_set.add(each[:i] + "()" + each[i:])
            self.helper(n - 1, total_set, new_set)

s = Solution()
result = s.generateParenthesis(4)
print(result)
print(len(result))


