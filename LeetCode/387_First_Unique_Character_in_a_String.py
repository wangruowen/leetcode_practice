# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return 0

        index_map = {}
        for i, c in enumerate(s):
            if c in index_map:
                index_map[c] = - 1
            else:
                index_map[c] = i
        min_i = len(s)
        for c in index_map:
            if index_map[c] >= 0:
                min_i = min(min_i, index_map[c])
        return min_i if min_i < len(s) else -1

