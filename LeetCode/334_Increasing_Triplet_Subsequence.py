# https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a,b,c = float('inf'), float('inf'), float('inf')
        for each in nums:
            a = min(a, each)
            if each > a:
                b = min(b, each)
            if each > b:
                return True

        return False
