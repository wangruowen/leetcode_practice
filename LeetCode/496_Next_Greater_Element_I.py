# https://leetcode.com/problems/next-greater-element-i/description/
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Stack
        result = []
        for each in findNums:
            i = nums.index(each)
            for j in range(i + 1, len(nums)):
                if nums[j] > each:
                    result.append(nums[j])
                    break
            else:
                result.append(-1)
        return result