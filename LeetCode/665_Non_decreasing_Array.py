# https://leetcode.com/problems/non-decreasing-array/description/
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1: return True

        # Find the wrong pair first, if there are two, return False directly
        last = nums[0]
        wrong_index = -1
        for i in xrange(1, len(nums)):
            if last > nums[i]:
                if wrong_index >= 0:
                    return False
                wrong_index = i - 1
            last = nums[i]

        # print(wrong_index)
        # (wrong_index, wrong_index + 1)
        # 1. If wrong_index is the first pair or the last pair, we can
        # always modify the first value or the last value
        # 2. Change the first one to be the same as second one
        # nums[wrong_index] = nums[wrong_index + 1]
        # 3. Change the second one to be the same as first one
        # nums[wrong_index + 1] = nums[wrong_index]
        if wrong_index > 0 and wrong_index < len(nums) - 2 and \
                nums[wrong_index - 1] > nums[wrong_index + 1] and \
                nums[wrong_index] > nums[wrong_index + 2]:
            return False

        return True



s = Solution()
# a = [3,4,2,3]
# a = [2,6,4,5]
a = [1,2,4,5,3]
print(s.checkPossibility(a))
