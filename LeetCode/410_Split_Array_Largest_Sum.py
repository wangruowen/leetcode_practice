# https://leetcode.com/problems/split-array-largest-sum/description/
class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # DP
        # dp[m][i] is the min of largest sum among m subarrays from nums[i:]
        # dp[m][i] = min(max(sum(nums[i:j]), dp[m-1][j])), where i+1 <= j <= len(nums) - m
        len_nums = len(nums)
        if len_nums <= m:
            return max(nums)

        dp = [[0 for _ in range(len_nums)] for _ in range(m)]
        sum_nums = [0]
        for each in nums:
            sum_nums.append(sum_nums[-1] + each)
        # print(sum_nums)

        for i in range(len_nums):
            dp[0][i] = sum_nums[len_nums] - sum_nums[i]
            # print("dp[%d][%d] = %d" % (1, i, dp[1][i]))

        for k in range(1, m):
            for i in range(len_nums - k):
                dp[k][i] = float('inf')
                for j in range(i + 1, len_nums - k + 1):
                    tmp = max(sum_nums[j] - sum_nums[i], dp[k-1][j])
                    if tmp < dp[k][i]:
                        dp[k][i] = tmp
                    else:
                        break
                # print("dp[%d][%d] = %d" % (k, i, dp[k][i]))

        return dp[-1][0]


s = Solution()
nums = [2,3,1,2,4,3]
m = 5
print(s.splitArray(nums, m))
