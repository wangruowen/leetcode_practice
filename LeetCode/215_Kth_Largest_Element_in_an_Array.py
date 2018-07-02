# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Priority Queue, using heapq, pop len(nums) - k
        # heapify: O(log n), heappop: O(log n), heappush: O(log n)
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums, k))