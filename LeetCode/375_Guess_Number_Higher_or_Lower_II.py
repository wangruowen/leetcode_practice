# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP
        # dp[i][j] is the min money to guarantee win for [i, j] inclusive.
        # Once we pick k, we know it is higher or lower, then the sub-problem is the worse one
        # of from i to k - 1, or from k + 1 to j
        # dp[i][j] = min(i <= k <= j max(dp[i][k - 1], dp[k + 1][j]))
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][i] = 0
            if i != n:
                dp[i][i + 1] = i

        for length in range(2, n):  # length from 2 to n - 1
            for i in range(1, n - length + 1):
                j = i + length
                for k in range(i, j + 1):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1] if k - 1 > i else 0,
                                                     dp[k + 1][j] if k + 1 < j else 0))

        return dp[1][n]

s = Solution()
print(s.getMoneyAmount(10))