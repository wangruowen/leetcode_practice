# https://leetcode.com/problems/longest-uncommon-subsequence-i/description/
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # as long as they are not the same, they are uncommon
        return max(len(a), len(b)) if a != b else -1