# https://leetcode.com/problems/subsets/description/
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for each in nums:
            tmp = []
            for each_set in result:
                dup_set = each_set[:]
                dup_set.append(each)
                tmp.append(dup_set)
            result.extend(tmp)
        return result

s = Solution()
nums = [1,2,3]
print(s.subsets(nums))
