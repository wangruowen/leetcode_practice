# https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Because we cannot modify the array
        # we cannot use O(n) extra, so we cannot sort
        # We need to use Binary Search from 1 to n, given n + 1 len list
        return self.helper(nums, 1, len(nums) - 1)

    def helper(self, nums, start, end):
        if start == end:
            return start

        mid = (start + end) // 2
        if sum(x <= mid for x in nums) > mid:
            return self.helper(nums, start, mid)
        else:
            return self.helper(nums, mid + 1, end)
