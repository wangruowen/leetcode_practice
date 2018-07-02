# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        last_idx, already_had_two = 0, False  # the first item
        i = 1
        while i < len(nums):
            if nums[i] == nums[last_idx]:
                if not already_had_two:
                    last_idx += 1
                    nums[last_idx] = nums[i]
                    already_had_two = True
            else:
                already_had_two = False
                last_idx += 1
                nums[last_idx] = nums[i]
            i += 1

        return last_idx + 1

s = Solution()
nums = [1,1,1,1,2,2,2,3,3,3]
print(s.removeDuplicates(nums))
print(nums)