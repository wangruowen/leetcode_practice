# https://leetcode.com/problems/relative-ranks/description/
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort_nums = sorted(nums)[::-1]
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        num_rank_dict = dict(zip(sort_nums, ranks))
        return map(num_rank_dict.get, nums)


