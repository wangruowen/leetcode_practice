# https://leetcode.com/problems/third-maximum-number/description/
class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_top, max_sec, max_third = float('-inf'), None, None
        for each in set(nums):
            if each > max_top:
                max_third = max_sec
                max_sec = max_top
                max_top = each
            elif each > max_sec:
                max_third = max_sec
                max_sec = each
            elif each > max_third:
                max_third = each
        return max_third if max_third is not None and max_third != float('-inf') else max_top
