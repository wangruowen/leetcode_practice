# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        init_sum = sum(nums)
        n = len(nums)
        min_num = min(nums)
        # init_sum + m * (n - 1) = (min_num + m) * n
        # m = init_sum - min_num * n
        return init_sum - min_num * n
