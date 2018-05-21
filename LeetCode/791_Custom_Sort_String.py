# https://leetcode.com/problems/custom-sort-string/description/
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # The goal is to make S is a subsequence of T
        # Pick the letters need to be re-ordered
        result = []
        t_map = {}
        for each in T:
            t_map[each] = t_map.get(each, 0) + 1

        for each in S:
            if each in t_map:
                result.append(each * t_map[each])
                t_map[each] = -1
        for each in t_map:
            if t_map[each] != -1:
                result.append(each * t_map[each])
        return "".join(result)




