# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        last = 0
        for each in nums:
            if nums[last] != each:
                last += 1
                nums[last] = each
        return last + 1

    def removeDuplicates_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, cur = 0, 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            nums[cur] = nums[i]
            cur += 1
            i += 1
        return cur

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)
