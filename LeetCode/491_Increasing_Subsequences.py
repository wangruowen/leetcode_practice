# https://leetcode.com/problems/increasing-subsequences/description/
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(len(nums) - 1):
            queue = [tuple([nums[i]])]
            for j in xrange(i + 1, len(nums)):
                new_queue = []
                for each_array in queue:
                    if nums[j] >= each_array[-1]:
                        new_array = list(each_array)
                        new_array.append(nums[j])
                        new_queue.append(tuple(new_array))
                queue.extend(new_queue)
                result.extend(new_queue)

        return [list(x) for x in set(result)]

s = Solution()
a = [4,6,7,7]
print(s.findSubsequences(a))
