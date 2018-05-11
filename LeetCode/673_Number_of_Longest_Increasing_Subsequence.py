# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        # DP
        # dp[i][0] refers to the number of max-len increasing subsequences end with the i-th item
        # dp[i][1] refers to the max length of the increasing subsequences end with the i-th item
        dp = [[1, 1] for _ in nums]
        # Initialize dp as initial max length is 1 and initial num of such subseq is 1
        max_len = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j][1] + 1 > dp[i][1]:
                        # if j's max length + 1 is longer than i's
                        # update i's max length with this new length
                        # and assign j's num of len to i's
                        dp[i][1] = dp[j][1] + 1
                        dp[i][0] = dp[j][0]
                    elif dp[j][1] + 1 == dp[i][1]:
                        # if j's max length + 1 is equal to i's
                        # that means i's max length is already assigned by previous j
                        # just add up the num of sam len
                        dp[i][0] += dp[j][0]
                    # if j's max length is smaller than current i's, ignore
            max_len = max(max_len, dp[i][1])

        count = 0
        for each_num, each_len in dp:
            if each_len == max_len:
                count += each_num
        return count



s = Solution()
a = \
[4,20,7,22,14,63,58,75,32,35,30,86,91,23,38,31,5,93,37,96,49,91,96,53,23,1,93,59,20,7,39,49,37,97,87,19,78,100,30,50,78,80,41,42,91,92,26,72,21,52,51,57,31,58,29,72,55,64,97,90,76,80,69,11,3,56,90,98,46,83,91,46,20,17,84,2,16,64,25,99]


print(s.findNumberOfLIS(a))




