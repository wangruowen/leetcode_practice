class Solution(object):
    def singleNumber(self, nums):
        """
        Using XOR

        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for each in nums:
            result ^= each
        return result
