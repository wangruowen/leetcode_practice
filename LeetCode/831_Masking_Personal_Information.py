# https://leetcode.com/problems/masking-personal-information/description/
import re

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        email_pattern = r'([a-zA-Z]{2,})@([a-zA-Z]+)\.([a-zA-Z]+)'
        country_phone_pattern = r'([0-9]{1,3})([0-9]{3})([0-9]{3})([0-9]{4})'
        local_phone_pattern = r'([0-9]{3})([0-9]{3})([0-9]{4})'
        m = re.match(email_pattern, S)
        if m:
            name1, name2, name3 = m.group(1).lower(), m.group(2).lower(), m.group(3).lower()
            return name1[0] + "*" * 5 + name1[-1] + "@" + name2 + "." + name3

        S = re.sub(r'[\+\(\)\- ]', '', S)
        print(S)
        if len(S) == 10:
            m = re.match(local_phone_pattern, S)
            n3 = m.group(3)
            return "***-***-" + n3
        else:
            m = re.match(country_phone_pattern, S)
            n1, n4 = m.group(1), m.group(4)
            return "+" + "*" * len(n1) + "-***-***-" + n4

s = Solution()
S = ["30(6081)-0-456", "LeetCode@LeetCode.com", "AB@qq.com", "1(234)567-890", "86-(10)12345678"]
for each in S:
    print(s.maskPII(each))