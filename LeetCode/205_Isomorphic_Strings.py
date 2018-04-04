# https://leetcode.com/problems/isomorphic-strings/description/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0: return True
        mapping = {}
        visited_set = set()
        for i in xrange(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            elif t[i] in visited_set:
                return False
            else:
                mapping[s[i]] = t[i]
                visited_set.add(t[i])

        return True

