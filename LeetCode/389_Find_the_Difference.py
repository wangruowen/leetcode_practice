# https://leetcode.com/problems/find-the-difference/description/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letter_map = {}
        for c in s:
            letter_map[c] = letter_map.get(c, 0) + 1
        for c in t:
            if c not in letter_map:
                return c
            else:
                letter_map[c] -= 1
        for c in letter_map:
            if letter_map[c] != 0:
                return c
