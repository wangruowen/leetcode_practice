# https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # HashMap with Prefix[j] - Prefix[i]
        result = 0
        prefix_sum_dict = defaultdict(int)
        sum_so_far = 0
        prefix_sum_dict[sum_so_far] += 1
        for each in nums:
            sum_so_far += each
            result += prefix_sum_dict[sum_so_far - k]
            prefix_sum_dict[sum_so_far] += 1
        return result