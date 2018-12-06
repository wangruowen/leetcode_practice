# https://leetcode.com/problems/burst-balloons/
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        # Basically, after bust some balloons, the subsequence array may already be visited
        # bottom up DP
        # https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
        # https://leetcode.com/problems/burst-balloons/discuss/76229/For-anyone-that-is-still-confused-after-reading-all-kinds-of-explanations...
        # dp[i][j] is the max coins after bust all balloons between i, j inclusive
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for k in range(2, n):
            for left in range(n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] +
                                          dp[left][i] + dp[i][right])
        return dp[0][-1]



