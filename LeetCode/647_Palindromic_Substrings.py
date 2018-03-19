# https://leetcode.com/problems/palindromic-substrings/description/
import pprint

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP
        # p[i][j] represents whether s[i:i + j] is palindrome, j is the length
        # 0 <= i < len(s), 0 < j <= len(s)
        p = [[False for _ in range(len(s) + 1)] for _ in range(len(s))]

        # Initialize p
        for i in range(len(s)):
            # s[i:i + 1] is single letter palindrome
            p[i][1] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                # s[i:i + 2]
                p[i][2] = True

        # Now start thinking about len >= 3 till len(s)
        for j in range(3, len(s) + 1):
            for i in range(len(s) - j + 1):
                if s[i] == s[i + j - 1]:
                    p[i][j] = p[i + 1][j - 2]

        # pprint.pprint(p)
        return sum(sum(x) for x in p)

a="aaaaa"
s = Solution()
print(s.countSubstrings(a))