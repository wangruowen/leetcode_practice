# https://leetcode.com/problems/reverse-string-ii/description/
import math

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        parts = int(math.ceil(len(s) / float(k)))
        for i in xrange(parts):
            cur_s = s[(k * i):(k * (i + 1))]
            if i % 2 == 0:
                result += cur_s[::-1]
            else:
                result += cur_s
        return result

s = Solution()
print(s.reverseStr("abcdefg", 2))