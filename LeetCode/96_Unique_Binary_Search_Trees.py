# https://leetcode.com/problems/unique-binary-search-trees/description/
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP
        # dp[i][j] is the num of unique BST between i to j, 1 <= i <= j <= n
        # dp[i][j] = sum(dp[i][k-1] * dp[k+1][j]) for every k, i <= k <= j
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][i] = 1
            if i < n:
                dp[i][i+1] = 2
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length
                for k in range(i, j + 1):
                    left, right = 1, 1
                    if k - 1 >= i:
                        left = dp[i][k - 1]
                    if k + 1 <= j:
                        right = dp[k + 1][j]
                    dp[i][j] += left * right
        return dp[1][n]

s = Solution()
print(s.numTrees(3))



