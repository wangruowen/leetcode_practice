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

    def subsetsWithDup_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        last_result = None
        for i in range(len(nums)):
            parent_result = result
            if i > 0 and nums[i] == nums[i-1]:
                parent_result = last_result
            new_result = []
            for each_set in parent_result:
                new_set = each_set[:]
                new_set.append(nums[i])
                new_result.append(new_set)
            result.extend(new_result)
            last_result = new_result
        return result


s = Solution()
nums = [3,1,2,2]
print(s.subsetsWithDup_v2(nums))