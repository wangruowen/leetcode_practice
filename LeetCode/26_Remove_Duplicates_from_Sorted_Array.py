# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[i]:
                if i + 1 < j:
                    nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i + 1

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))
print(nums)
