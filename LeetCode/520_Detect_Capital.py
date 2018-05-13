# https://leetcode.com/problems/detect-capital/description/
import re

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if re.match(r'^[A-Z]+$', word) or re.match(r'^[a-z]+$', word) or re.match(r'^[A-Z][a-z]+$', word):
            return True
        return False