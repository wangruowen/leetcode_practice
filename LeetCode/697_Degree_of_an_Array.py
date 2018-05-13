# https://leetcode.com/problems/degree-of-an-array/description/
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = {}
        for each in nums:
            num_count[each] = num_count.get(each, 0) + 1
        max_freq = 0
        max_nums = []
        for each in num_count:
            max_freq = max(max_freq, num_count[each])
        for each in num_count:
            if max_freq == num_count[each]:
                max_nums.append(each)
        # print(max_nums)

        min_len = len(nums)
        reverse_nums = nums[::-1]
        for each in max_nums:
            cur_len = len(nums) - reverse_nums.index(each) - nums.index(each)
            min_len = min(min_len, cur_len)
        return min_len

s = Solution()
a = [1,2,2,3,1]
print(s.findShortestSubArray(a))
