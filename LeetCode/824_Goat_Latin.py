# https://leetcode.com/problems/goat-latin/description/
import re

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        words = S.split()
        for i in range(len(words)):
            each = words[i]
            if re.match(r'^[aeiou].*', each.lower()):
                result.append(each + "ma" + "a" * (i + 1))
            else:
                result.append(each[1:] + each[0] + "ma" + "a" * (i + 1))
        return " ".join(result)
