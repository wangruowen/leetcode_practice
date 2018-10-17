# https://leetcode.com/problems/partition-equal-subset-sum/description/
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DP backpack problem
        # dp[i][j] is whether sum j can be got from nums[:i]
        # Either choose nums[i-1] or not choose
        # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        sum_nums //= 2
        dp = [[False for _ in range(sum_nums + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        for i in range(1, len(nums) + 1):
            for j in range(1, sum_nums + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][sum_nums]
