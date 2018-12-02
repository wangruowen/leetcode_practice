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

    def permuteUnique_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        def helper(rest_nums, stack=[]):
            if len(rest_nums) == 0:
                result.append(list(stack))
                return

            for j in range(len(rest_nums)):
                if j > 0 and rest_nums[j] == rest_nums[j - 1]:
                    continue
                stack.append(rest_nums[j])
                helper(rest_nums[:j] + rest_nums[j + 1:], stack)
                stack.pop()

        helper(nums)
        return result

s = Solution()
a = [1,1,2]
print(s.permuteUnique(a))