# https://leetcode.com/problems/target-sum/description/
from collections import defaultdict

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # DP
        # sum(P) - sum(N) = target
        # sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
        # 2 * sum(P) = target + sum(nums)
        # sum(P) = (target + sum(nums)) / 2
        sum_nums = sum(nums)
        if sum_nums < S or -sum_nums > S or (sum_nums + S) % 2 != 0:
            return 0
        sum_P = (sum_nums + S) // 2
        # Then this is reduced to the same problem of 416,
        # dp[i][j] is the number of ways that the sum of values picked from nums[:i] is j
        # 0 <= j <= sum_P
        # dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        dp_i_minus_1 = defaultdict(int)
        dp_i = defaultdict(int)
        dp_i_minus_1[0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(sum_P + 1):
                dp_i[j] = dp_i_minus_1[j]
                if j >= nums[i - 1]:
                    dp_i[j] += dp_i_minus_1[j - nums[i-1]]
            dp_i_minus_1 = dp_i
            dp_i = defaultdict(int)

        return dp_i_minus_1[sum_P]

s = Solution()
nums = [1, 1, 1, 1, 1]
target = 3
print(s.findTargetSumWays(nums, target))

