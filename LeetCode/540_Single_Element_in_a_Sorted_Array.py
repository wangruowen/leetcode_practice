# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A better way is Binary Search
        result = 0
        for each in nums:
            result ^= each
        return result

s = Solution()
a = [1,1,2,3,3,4,4,5,5]
print(s.singleNonDuplicate(a))