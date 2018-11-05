# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if target < nums[mid]:
                j = mid - 1
            elif target > nums[mid]:
                i = mid + 1
            else:
                # mid is in the range of target
                break

        if i > j:
            return -1, -1

        # mid of [i, j] contains target
        # We need to find the starting and ending points
        t_start = mid
        # t_start can also be treated as the exclusive end of less-than-target
        t_end = mid
        # t_end can be treated as the exclusive start of greater-than-target
        while i < t_start:
            mid = (i + t_start) // 2
            if target == nums[mid]:
                t_start = mid
            elif target > nums[mid]:
                i = mid + 1
        while t_end <= j:
            mid = (t_end + j) // 2
            if target < nums[mid]:
                j = mid - 1
            elif target == nums[mid]:
                t_end = mid + 1

        return t_start, t_end - 1

s = Solution()
nums = [8,8,8,8]
target = 8
print(s.searchRange(nums, target))

