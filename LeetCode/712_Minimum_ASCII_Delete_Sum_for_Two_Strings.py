# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # DP
        # dp[i][j] is the lowest ASCII cost for s1[:i] (last one is s1[i -1]) and s2[:j] (last one is s2[j - 1])
        # if s1[i] == s2[j]: dp[i + 1][j + 1] = dp[i][j]
        # if s1[i] != s2[j]: dp[i + 1][j + 1] =
        #     min(dp[i + 1][j] + s2[j] /*keep s1[i], delete s2[j]*/,
        #         dp[i][j + 1] + s1[i] /*keep s2[j], delete s1[i]*/)
        dp = [[0 for _ in xrange(len(s2) + 1)] for _ in xrange(len(s1) + 1)]
        for j in xrange(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in xrange(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            for j in xrange(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + ord(s2[j - 1]), dp[i - 1][j] + ord(s1[i - 1]))

        return dp[-1][-1]
