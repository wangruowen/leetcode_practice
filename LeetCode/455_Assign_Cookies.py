# https://leetcode.com/problems/assign-cookies/description/
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # Simple Greedy For cur least greed child, find the least s cookie
        g.sort()
        s.sort()
        count = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
            j += 1
        return count
