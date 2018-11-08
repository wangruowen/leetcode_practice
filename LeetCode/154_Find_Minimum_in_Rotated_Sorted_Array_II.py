# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                while mid <= right and nums[mid] == nums[right]:
                    right -= 1
            else:
                right = mid - 1
        return nums[0]


s = Solution()
nums = [4,5,6,7,0,1,2]
print(s.findMin(nums))
