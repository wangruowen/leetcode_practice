# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [x[0] for x in Counter(nums).most_common(k)]
