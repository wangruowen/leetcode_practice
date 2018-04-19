# https://leetcode.com/problems/jump-game/description/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1: return True
        # If there is no zero, definitely we can reach the end
        if 0 not in nums:
            return True

        # If there are zeros, we need to jump over them
        # The values before zero should "index + val" > zero_index
        # identify all zeros indices
        zero_indices = []
        for i in xrange(len(nums) - 1):
            if nums[i] == 0:
                zero_indices.append(i)

        for each_zero_index in zero_indices:
            jump_over_zero = False
            for i in xrange(1, each_zero_index + 1):
                if nums[each_zero_index - i] + each_zero_index - i > each_zero_index:
                    # We can jump over
                    jump_over_zero = True
                    break
            if not jump_over_zero:
                return False

        return True

