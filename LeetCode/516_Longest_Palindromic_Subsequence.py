# https://leetcode.com/problems/longest-palindromic-subsequence/description/
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)

        # DP
        # dp[i][j] keeps all the longest palindromic subsequences from i to j inclusive
        # 0 <= i/j <= len(s) - 1, we want to get dp[0][n - 1]

        # dp[i][j] = the max-len palindrome of the following three cases
        #       1. s[i] == s[j] => s[i] + dp[i + 1][j - 1] + s[j]
        #       2. s[i] == s[p] where p < j, which should be dp[i][j - 1]
        #       3. s[j] == s[q] where q > i, which should be dp[i + 1][j]
        dp = [[1 for _ in range(len(s))] for _ in range(len(s))]

        # Initialize, single-length letter
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                # two letters
                dp[i][i + 1] = 2

        # from 3 letters to length n
        for l in range(2, len(s)):
            for i in range(len(s) - l):
                j = i + l
                # dp[i][j]
                # Case 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Case 2
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]

s = Solution()
S = \
"hiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxrhiddqscdxr"

print(s.longestPalindromeSubseq(S))




