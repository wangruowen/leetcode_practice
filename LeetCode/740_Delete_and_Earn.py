# https://leetcode.com/problems/delete-and-earn/description/
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort and DP
        # Basically, we can pick every other item
        counter = Counter(nums)
        ordered_items = sorted(counter.keys())
        points = [0] * 10001
        for each in ordered_items:
            points[each] = counter[each] * each
        # dp_i = max(dp_i_2 + points[i], dp_i_1)
        dp_i_2, dp_i_1, dp_i = 0, 0, 0
        for each in points:
            dp_i = max(dp_i_2 + each, dp_i_1)
            dp_i_2, dp_i_1 = dp_i_1, dp_i
        return dp_i




