# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()
        return " ".join(reversed(s))