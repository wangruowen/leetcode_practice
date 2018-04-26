# https://leetcode.com/problems/subsets-ii/description/
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set([tuple()])
        for each in sorted(nums):
            tmp_set = set()
            for each_tuple in result:
                dup_tuple = list(each_tuple)
                dup_tuple.append(each)
                tmp_set.add(tuple(dup_tuple))
            result = result.union(tmp_set)
            print(tmp_set)

        return [list(each_set) for each_set in result]

s = Solution()
nums = [1,2,2]
print(s.subsetsWithDup(nums))