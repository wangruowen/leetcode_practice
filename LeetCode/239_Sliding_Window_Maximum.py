# https://leetcode.com/problems/sliding-window-maximum/description/
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Monotonic Queue, which is monotonically increasing or decreasing
        max_nums = []
        queue = deque()
        for i, c in enumerate(nums):
            while queue and c > nums[queue[-1]]:
                # If cur num is bigger than the last few in queue
                # get rid of these small ones in the queue, because
                # they will never be max num in a sliding window, since
                # the current num will take over them

                # In this way, the queue is kept in a decreasing order
                # And the first one is the max value
                queue.pop()
            queue.append(i)
            if i >= k and queue and queue[0] == i - k:
                # The sliding is k-size full, and i is k + 1
                # If the first one in the queue is the max of the queue
                # we have to pop it out because it will no longer be in the queue
                # Note that, it doesn't matter whether the queue is k-full or not
                # As long as the queue[0] == i - k, we have to pop it out
                # because next slide will exclude this i - k
                queue.popleft()

            if i >= k - 1:
                # Start from the first sliding window is k-full
                # we store the max of each sliding
                max_nums.append(nums[queue[0]])

        return max_nums

