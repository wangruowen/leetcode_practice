# https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = s.split()
        return len(tokens[-1]) if len(tokens) > 0 else 0