# https://leetcode.com/problems/beautiful-arrangement/description/
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0
        self.helper([], list(range(1, N + 1)))
        return self.count

    def helper(self, used_values, rest_values):
        i = len(used_values) + 1
        if len(rest_values) == 0:
            self.count += 1

        for each in rest_values:
            if i % each == 0 or each % i == 0:
                used_values.append(i)
                new_rest = rest_values[:]
                new_rest.remove(each)
                self.helper(used_values, new_rest)
                used_values.pop()
