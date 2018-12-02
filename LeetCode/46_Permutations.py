# https://leetcode.com/problems/permutations/description/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Backtrack
        self.total_set = []
        self.helper(nums)

        return self.total_set

    def helper(self, nums, perm_set=[]):
        if len(nums) == 0:
            self.total_set.append(perm_set)
            return

        for i in range(len(nums)):
            new_set = perm_set[:]
            new_set.append(nums[i])
            self.helper(nums[:i] + nums[i + 1:], new_set)

    def permute_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def helper(rest_nums, stack=[]):
            if not rest_nums:
                result.append(stack[:])

            for i in rest_nums:
                new_rest_nums = set(rest_nums)
                new_rest_nums.remove(i)
                stack.append(i)
                helper(new_rest_nums, stack)
                stack.pop()

        helper(nums)
        return result