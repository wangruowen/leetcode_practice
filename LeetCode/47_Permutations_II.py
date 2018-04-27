# https://leetcode.com/problems/permutations-ii/description/
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Backtrack
        self.total_set = set()
        self.helper(nums)

        return [list(x) for x in self.total_set]


    def helper(self, nums, perm_set=[]):
        if len(nums) == 0:
            self.total_set.add(tuple(perm_set))
            return

        for i in range(len(nums)):
            new_set = perm_set[:]
            new_set.append(nums[i])
            self.helper(nums[:i] + nums[i + 1:], new_set)

s = Solution()
a = [1,1,2]
print(s.permuteUnique(a))