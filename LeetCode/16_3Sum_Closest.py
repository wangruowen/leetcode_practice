# https://leetcode.com/problems/3sum-closest/description/
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff = float('inf')
        result = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip dup ones
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                cur_diff = nums[i] + nums[j] + nums[k] - target
                if abs(cur_diff) < min_diff:
                    min_diff = abs(cur_diff)
                    result = cur_diff + target
                if cur_diff < 0:
                    # less than target
                    j += 1
                elif cur_diff > 0:
                    # bigger than target
                    k -= 1
                else:
                    # exactly target
                    return target
        return result
