# https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Binary Search
        # bisect_left
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if start == len(nums):
            return start
        elif nums[start] > target:
            return start
        else:
            return start + 1

s = Solution()
nums = [1,4]
target = 3
print(s.searchInsert(nums, target))