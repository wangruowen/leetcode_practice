# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        last_index = 0
        for each in nums:
            if each != val:
                nums[last_index] = each
                last_index += 1
        return last_index

s = Solution()
nums = [1, 2, 3, 4, 5, 2, 2]
target = 2
print(s.removeElement(nums, target))
print(nums)