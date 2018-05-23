# https://leetcode.com/problems/optimal-division/description/
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # the answer is always X1/(X2/X3/../Xn) = (X1 *X3 *..*Xn)/X2
        if len(nums) <= 2:
            return "/".join(map(str, nums))
        return "%s/(%s)" % (str(nums[0]), "/".join(map(str, nums[1:])))
