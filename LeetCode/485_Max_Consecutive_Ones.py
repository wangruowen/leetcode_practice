# https://leetcode.com/problems/max-consecutive-ones/description/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        cur_start = -1
        for i, each in enumerate(nums):
            if each == 1:
                if cur_start < 0:
                    cur_start = i
            elif cur_start >= 0:
                max_len = max(i - cur_start, max_len)
                cur_start = -1
        if each == 1:
            # the last one is still 1
            max_len = max(len(nums) - cur_start, max_len)
        return max_len

s = Solution()
print(s.findMaxConsecutiveOnes([0]))